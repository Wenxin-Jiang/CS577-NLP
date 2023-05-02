import torch
import random
import json
import csv
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader
from torch import nn
from datasets import load_dataset, Dataset, concatenate_datasets
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, TrainingArguments, \
    Trainer, BertForQuestionAnswering, AdamW, BertTokenizerFast, BertModel, BertConfig, \
        BertTokenizer, BertPreTrainedModel
from collections import Counter
from sklearn.metrics import f1_score
from transformers.data.metrics.squad_metrics import compute_exact, compute_f1

import os
os.environ["WANDB_DISABLED"] = "true"

# TODO: If the answer is not in the vocabulary, we will not have any output. Same as the input

from loguru import logger

def clean_context(context):
    # Remove yaml structure
    context = re.sub(r'^---\n[\s\S]*?---\n', '', context)
    
    # Remove tables
    context = re.sub(r'\|[\s\S]*?\|', '', context)
    
    return context.strip()


def remove_padding(text, tokenizer):

    tokens = tokenizer.tokenize(text)
    if not tokens:
        return text
    first_token = tokens[0]
    last_token = tokens[-1]
    if first_token == tokenizer.pad_token:
        tokens = tokens[1:]
    if last_token == tokenizer.pad_token:
        tokens = tokens[:-1]
    return tokenizer.convert_tokens_to_string(tokens)


def clean_answer(answer, tokenizer):
    logger.debug(f"answer: {answer}")
    answer = answer.lower()  # Convert to lowercase
    answer = re.sub(r"[^a-z0-9\s]", "", answer)  # Remove non-alphanumeric characters
    answer = re.sub(r"\s+", " ", answer)  # Collapse multiple whitespaces
    answer = answer.strip()  # Remove leading/trailing whitespaces
    logger.debug(f"answer after clean: {answer}")
    logger.debug(f"answer after remove padding: {tokenizer.convert_tokens_to_string(remove_padding(answer, tokenizer))}")
    return remove_padding(answer, tokenizer)



class MyQAModel(BertPreTrainedModel):
    def __init__(self, config):
        super().__init__(config)
        self.bert = BertModel(config)
        self.qa_outputs = nn.Linear(config.hidden_size, 2)
        self.dropout = nn.Dropout(config.hidden_dropout_prob)
        self.init_weights()

    def forward(self, input_ids, attention_mask=None, token_type_ids=None, start_positions=None, end_positions=None):
        bert_outputs = self.bert(input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)
        sequence_output = bert_outputs[0]

        # You can add custom layers or modify the architecture here if needed.

        sequence_output = self.dropout(sequence_output)
        logits = self.qa_outputs(sequence_output)
        start_logits, end_logits = logits.split(1, dim=-1)
        start_logits = start_logits.squeeze(-1)
        end_logits = end_logits.squeeze(-1)

        if start_positions is not None and end_positions is not None:
            loss_fct = nn.CrossEntropyLoss()
            start_loss = loss_fct(start_logits, start_positions)
            end_loss = loss_fct(end_logits, end_positions)
            total_loss = (start_loss + end_loss) / 2
            return total_loss
        else:
            return start_logits, end_logits

def preprocess_data(dataset, max_length):
    tokenized_data = []
    for item in dataset:
        for qa in item['paragraphs'][0]['qas']:
            question = qa['question']
            context = item['paragraphs'][0]['context']
            char_start_position = qa['answers'][0]['answer_start']
            char_end_position = char_start_position + len(qa['answers'][0]['text'])

            inputs = tokenizer.encode_plus(question, context, add_special_tokens=True, max_length=max_length, padding='max_length', truncation=True, return_offsets_mapping=True)
            input_ids, token_type_ids, attention_mask, offsets_mapping = inputs["input_ids"], inputs["token_type_ids"], inputs["attention_mask"], inputs["offset_mapping"]

            token_start_position = None
            token_end_position = None
            for i, offsets in enumerate(offsets_mapping):
                if token_start_position is None and offsets[0] == char_start_position:
                    token_start_position = i
                if offsets[1] == char_end_position:
                    token_end_position = i
                    break

            if token_start_position is not None and token_end_position is not None:
                logger.info(f"Token positions found for answer: {qa['answers'][0]['text']}")
                tokenized_data.append({
                    'input_ids': torch.tensor(input_ids, dtype=torch.long),
                    'token_type_ids': torch.tensor(token_type_ids, dtype=torch.long),
                    'attention_mask': torch.tensor(attention_mask, dtype=torch.long),
                    'start_positions': torch.tensor(token_start_position, dtype=torch.long),
                    'end_positions': torch.tensor(token_end_position, dtype=torch.long)
                })
            else:
                logger.info(f"Token positions not found for answer: {qa['answers'][0]['text']}")

    return tokenized_data





def compute_exact_match(true_labels, pred_labels):
    total = len(true_labels)
    correct = sum([true == pred for true, pred in zip(true_labels, pred_labels)])
    exact_match = correct / total
    return exact_match

def compute_f1_score(true_labels, pred_labels):
    f1_scores = [f1_score(true, pred) for true, pred in zip(true_labels, pred_labels)]
    avg_f1_score = np.mean(f1_scores)
    return avg_f1_score

def f1_score(true, pred):
    common = set(true).intersection(set(pred))
    if not common:
        return 0
    precision = len(common) / len(pred)
    recall = len(common) / len(true)
    f1 = 2 * (precision * recall) / (precision + recall)
    return f1


def evaluate(model, data_loader):
    model.eval()
    all_start_logits = []
    all_end_logits = []
    all_start_positions = []
    all_end_positions = []
    
    with torch.no_grad():
        for batch in data_loader:
            input_ids = torch.stack(batch['input_ids']).transpose(0, 1).to(device)
            attention_mask = torch.stack(batch['attention_mask']).transpose(0, 1).to(device)
            start_positions = batch['start_positions'].clone().detach().to(device)
            end_positions = batch['end_positions'].clone().detach().to(device)

            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)

            start_logits, end_logits = model(input_ids, attention_mask=attention_mask)

            all_start_logits.extend(start_logits.cpu().numpy())
            all_end_logits.extend(end_logits.cpu().numpy())
            all_start_positions.extend(start_positions.cpu().numpy())
            all_end_positions.extend(end_positions.cpu().numpy())

    start_positions_preds = np.argmax(all_start_logits, axis=-1)
    end_positions_preds = np.argmax(all_end_logits, axis=-1)
    true_labels = list(zip(all_start_positions, all_end_positions))
    pred_labels = list(zip(start_positions_preds, end_positions_preds))

    exact_match = compute_exact_match(true_labels, pred_labels)
    f1_score = compute_f1_score(true_labels, pred_labels)

    return pred_labels, true_labels, exact_match, f1_score



# # Extract questions, contexts, and answers
# def process_dataset(split_dataset, split):
#     examples = []

#     for i in range(len(split_dataset)):
#         paragraphs = split_dataset[i]["paragraphs"]
#         for paragraph in paragraphs:
#             qas = paragraph["qas"]
#             context = paragraph["context"]
#             original_context = context
#             context = clean_context(context)
#             for qa in qas:
#                 question = qa["question"]
#                 answer_text = qa["answers"][0]["text"]
#                 answer_start = qa["answers"][0]["answer_start"]
#                 answer_end = answer_start + len(answer_text)
#                 new_answer_start, new_answer_end = update_answer_positions(context, answer_start, answer_end, original_context)
#                 examples.append({"question": question, "context": context, "answer_text": answer_text, "start_positions": new_answer_start, "end_positions": new_answer_end, "original_context": original_context})
#     tokenized_examples = {"input_ids": [], "attention_mask": [], "token_type_ids": [], "start_positions": [], "end_positions": [], "answer_input_ids": []}
#     for example in examples:
#         encoded_example = tokenizer.encode_plus(example["question"], example["context"], max_length=512, padding="max_length", truncation=True, return_tensors="pt")
#         tokenized_examples["input_ids"].append(encoded_example["input_ids"][0])
#         tokenized_examples["attention_mask"].append(encoded_example["attention_mask"][0])
#         tokenized_examples["token_type_ids"].append(encoded_example["token_type_ids"][0])
#         tokenized_examples["start_positions"].append(torch.tensor(example["start_positions"]).unsqueeze(0))
#         tokenized_examples["end_positions"].append(torch.tensor(example["end_positions"]).unsqueeze(0))
#         answer_input_ids = tokenizer.encode(example["answer_text"], add_special_tokens=False, return_tensors="pt")
#         # logger.debug(answer_input_ids.shape[1])
#         answer_input_ids = torch.cat([answer_input_ids[0], torch.zeros((16 - answer_input_ids.shape[1]), dtype=torch.long)], dim=0)
#         tokenized_examples["answer_input_ids"].append(answer_input_ids)
#     for k in tokenized_examples:
#         if k not in ["answer_start", "answer_end"]:
#             tokenized_examples[k] = torch.stack(tokenized_examples[k])
#         else:
#             tokenized_examples[k] = torch.cat(tokenized_examples[k], dim=0)
#     return tokenized_examples


# def evaluate(model, dataloader):
#     model.eval()
#     predictions = []
#     true_labels = []
#     total_exact_match = 0
#     total_f1_score = 0

#     with torch.no_grad():
#         for batch in dataloader:
#             input_ids = torch.stack(batch['input_ids']).transpose(0, 1)
#             attention_mask = torch.stack(batch['attention_mask']).transpose(0, 1)
#             start_positions = torch.cat(batch['start_positions'], dim=0).view(-1)
#             end_positions = torch.cat(batch['end_positions'], dim=0).view(-1)
#             answer_input_ids = torch.stack(batch['answer_input_ids']).transpose(0, 1)

#             input_ids = input_ids.to(device)
#             attention_mask = attention_mask.to(device)
#             start_positions = start_positions.to(device)
#             end_positions = end_positions.to(device)
#             answer_input_ids = answer_input_ids.to(device)

#             outputs = model(input_ids=input_ids, attention_mask=attention_mask, start_positions=start_positions, end_positions=end_positions)

#             start_logits, end_logits = outputs.start_logits, outputs.end_logits
#             start_indices = torch.argmax(start_logits, dim=1)
#             end_indices = torch.argmax(end_logits, dim=1)

#             for i, (start_index, end_index) in enumerate(zip(start_indices, end_indices)):
#                 input_id = input_ids[i]

#                 sep_index = (input_id == tokenizer.sep_token_id).nonzero(as_tuple=True)[0][0]
#                 start_index = max(start_index - sep_index - 1, 0)
#                 end_index = max(end_index - sep_index - 1, 0)

#                 predicted_answer = tokenizer.decode(input_id[sep_index + 1:][start_index:end_index + 1])
#                 true_answer = tokenizer.decode(answer_input_ids[i])

#                 exact_match = compute_exact(true_answer, predicted_answer)
#                 f1_score = compute_f1(true_answer, predicted_answer)

#                 predictions.append(predicted_answer)
#                 true_labels.append(true_answer)

#                 total_exact_match += exact_match
#                 total_f1_score += f1_score

#     num_samples = len(dataloader.dataset)
#     average_exact_match = total_exact_match / num_samples
#     average_f1_score = total_f1_score / num_samples

#     return predictions, true_labels, average_exact_match, average_f1_score





def generate_predicted_answers(data, predictions):
    predicted_answers = []
    for paragraph in data["data"][0]["paragraphs"]:
        for i, qa in enumerate(paragraph["qas"]):
            start_pred, end_pred = predictions[i]
            context = paragraph["context"]
            predicted_answer = context[start_pred:end_pred+1]
            predicted_answers.append(predicted_answer)
    return predicted_answers


def update_answer_positions(context, answer_start, answer_end, original_context):
    new_answer_start = context.find(original_context[answer_start:answer_start + 20])
    new_answer_end = new_answer_start + (answer_end - answer_start)

    return new_answer_start, new_answer_end


if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # raw_dataset = load_dataset("json", data_files={"train": "/depot/davisjam/data/wenxin/CS577-NLP/project/squad_format_data.json", "val": "/depot/davisjam/data/wenxin/CS577-NLP/project/squad_format_data.json"}, field="data")
    with open("/depot/davisjam/data/wenxin/CS577-NLP/project/QAmodel/updated_updated_squad_format_data.json", "r") as f:
        raw_dataset = json.load(f)
    
    
    # Randomly shuffle the dataset
    random.seed(577)
    random.shuffle(raw_dataset["data"])

    # Calculate the split indices
    data_size = len(raw_dataset["data"])
    logger.debug(f"Raw Dataset size: {data_size}")
    train_split_idx = int(data_size * 0.8)
    val_split_idx = int(data_size * 0.9)

    # Split the dataset into train, val, and test
    train_dataset = raw_dataset["data"][:train_split_idx]
    val_dataset = raw_dataset["data"][train_split_idx:val_split_idx]
    test_dataset = raw_dataset["data"][val_split_idx:]
    logger.info(f"Train dataset size: {len(train_dataset)}")
    logger.info(f"Val dataset size: {len(val_dataset)}")
    logger.info(f"Test dataset size: {len(test_dataset)}")

    # # Split the dataset into train, validation, and test sets
    # dataset = dataset['data'].train_test_split(test_size=0.2, seed=42)
    # train_val_dataset = dataset['train']
    # test_dataset = dataset['test']

    # train_val_dataset = train_val_dataset.train_test_split(test_size=0.125, seed=42)
    # train_dataset = train_val_dataset['train']
    # val_dataset = train_val_dataset['test']

    model_checkpoint = "bert-base-uncased"
    # model_checkpoint = "deepset/bert-base-cased-squad2"
    tokenizer = BertTokenizerFast.from_pretrained(model_checkpoint)
    # tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

    
        
    tokenized_train = preprocess_data(train_dataset, 512)
    tokenized_val = preprocess_data(val_dataset, 512)
    tokenized_test = preprocess_data(test_dataset, 512)

    # Convert dictionaries to Datasets
    tokenized_dataset_train = Dataset.from_list(tokenized_train)
    tokenized_dataset_val = Dataset.from_list(tokenized_val)
    tokenized_dataset_test = Dataset.from_list(tokenized_test)

    model = MyQAModel.from_pretrained(model_checkpoint)
    # If need to load model from checkpoint
    # model.load_state_dict(torch.load("model_epoch_1.pt"))  # Replace "model_epoch_1.pt" with the appropriate filename
    model = model.to(device)

    batch_size = 16
    train_loader = DataLoader(tokenized_dataset_train, batch_size=batch_size, shuffle=True)
    # train_loader = DataLoader(tokenized_dataset_val, batch_size=batch_size, shuffle=True) # TODO: Test only
    eval_loader = DataLoader(tokenized_dataset_val, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(tokenized_dataset_test, batch_size=batch_size, shuffle=True)
    lr = 2e-5
    num_epochs = 5
    optimizer = AdamW(model.parameters(), lr=lr)

    train_losses = []
    val_losses = []
    test_losses = []

    train_accuracies = []
    val_accuracies = []
    test_accuracies = []

    

    for epoch in range(num_epochs):
        model.train()
        train_loss = 0
        for i, batch in enumerate(train_loader):
            input_ids = torch.stack(batch['input_ids']).transpose(0, 1).to(device)
            attention_mask = torch.stack(batch['attention_mask']).transpose(0, 1).to(device)
            start_positions = batch['start_positions'].clone().detach().to(device)
            end_positions = batch['end_positions'].clone().detach().to(device)

            optimizer.zero_grad()
            # logger.debug(f"shape of input_ids: {input_ids.shape}")
            # logger.debug(f"shape of attention_mask: {attention_mask.shape}")
            # logger.debug(f"shape of start_positions: {start_positions.shape}")
            # logger.debug(f"shape of end_positions: {end_positions.shape}")

            loss = model(input_ids, attention_mask=attention_mask, start_positions=start_positions, end_positions=end_positions)
            loss.backward()
            optimizer.step()
            train_loss += loss.item()
            train_losses.append(loss.item())
            logger.info(f"Epoch {epoch+1}, Batch {i+1} - Loss: {loss.item():.4f}")

        avg_train_loss = train_loss / len(train_loader)

        # Eval loop
        model.eval()
        eval_loss = 0
        for i, batch in enumerate(eval_loader):
            input_ids = torch.stack(batch['input_ids']).transpose(0, 1).to(device)
            attention_mask = torch.stack(batch['attention_mask']).transpose(0, 1).to(device)
            start_positions = batch['start_positions'].clone().detach().to(device)
            end_positions = batch['end_positions'].clone().detach().to(device)

            with torch.no_grad():
                start_logits, end_logits = model(input_ids, attention_mask=attention_mask)
                loss = model(input_ids, attention_mask=attention_mask, start_positions=start_positions, end_positions=end_positions)

                eval_loss += loss.item()
                val_losses.append(loss.item())
                start_predictions = torch.argmax(start_logits, dim=1)
                end_predictions = torch.argmax(end_logits, dim=1)

        avg_eval_loss = eval_loss / len(eval_loader)

        logger.critical(f"Epoch {epoch+1} - Train loss: {avg_train_loss:.4f} - Eval loss: {avg_eval_loss:.4f}")
        torch.save(model.state_dict(), f"QA_BERT_epoch_{epoch+1}.pt")

        # Test Loop
        model.eval()
        test_loss = 0
        for i, batch in enumerate(test_loader):
            input_ids = torch.stack(batch['input_ids']).transpose(0, 1).to(device)
            attention_mask = torch.stack(batch['attention_mask']).transpose(0, 1).to(device)
            start_positions = batch['start_positions'].clone().detach().to(device)
            end_positions = batch['end_positions'].clone().detach().to(device)

            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)
            start_positions = start_positions.to(device)
            end_positions = end_positions.to(device)
            
            with torch.no_grad():
                start_logits, end_logits = model(input_ids, attention_mask=attention_mask)
                loss = model(input_ids, attention_mask=attention_mask, start_positions=start_positions, end_positions=end_positions)
                test_loss += loss.item()
                test_losses.append(loss.item())

        avg_test_loss = test_loss / len(test_loader)

        logger.critical(f"Epoch {epoch+1} - Train loss: {avg_train_loss:.4f} - Eval loss: {avg_eval_loss:.4f} - Test loss: {avg_test_loss:.4f}")

        exact_matches = []
        f1_scores = []
        train_exact_matches = []
        train_f1_scores = []
        val_exact_matches = []
        val_f1_scores = []
        test_exact_matches = []
        test_f1_scores = []

        train_preds, train_true_labels, train_exact_match, train_f1 = evaluate(model, train_loader)
        val_preds, val_true_labels, val_exact_match, val_f1 = evaluate(model, eval_loader)
        test_preds, test_true_labels, test_exact_match, test_f1 = evaluate(model, test_loader)

        logger.info(f"Train Exact Match: {train_exact_match:.4f}, Train F1 Score: {train_f1:.4f}")
        logger.info(f"Val Exact Match: {val_exact_match:.4f}, Val F1 Score: {val_f1:.4f}")
        logger.info(f"Test Exact Match: {test_exact_match:.4f}, Test F1 Score: {test_f1:.4f}")


        # logger.debug(f"train_predicted_indices: {train_preds}")
        # logger.debug(f"train_true_indices: {train_true_labels}")

        # logger.debug(f"val_predicted_indices: {val_preds}")
        # logger.debug(f"val_true_indices: {val_true_labels}")

        # logger.debug(f"test_predicted_indices: {test_preds}")
        # logger.debug(f"test_true_indices: {test_true_labels}")

        train_exact_matches.append(train_exact_match)
        val_exact_matches.append(val_exact_match)
        test_exact_matches.append(test_exact_match)

        train_f1_scores.append(train_f1)
        val_f1_scores.append(val_f1)
        test_f1_scores.append(test_f1)

    # Save train, val, and test predictions to CSV files
    # train_predictions_df = pd.DataFrame(train_preds, columns=["start_pred", "end_pred"])
    df = pd.DataFrame({'true_labels': train_true_labels, 'pred_labels': train_preds})
    df.to_csv("train_predictions.csv", index=False)

    df = pd.DataFrame({'true_labels': val_true_labels, 'pred_labels': val_preds})
    df.to_csv("val_predictions.csv", index=False)

    df = pd.DataFrame({'true_labels': test_true_labels, 'pred_labels': test_preds})
    df.to_csv("test_predictions.csv", index=False)
    
    input_texts = []  # Store the original input texts
    predicted_answers_train = []
    true_answers_train = []
    predicted_answers_val = []
    true_answers_val = []
    predicted_answers_test = []
    true_answers_test = []

    datasets = {
        "train": (train_loader, predicted_answers_train, true_answers_train),
        "val": (eval_loader, predicted_answers_val, true_answers_val),
        "test": (test_loader, predicted_answers_test, true_answers_test),
    }

    # for dataset_name, (data_loader, predicted_answers, true_answers) in datasets.items():
    #     for i, batch in enumerate(data_loader):
    #         input_ids = torch.stack(batch['input_ids']).transpose(0, 1).to(device)
    #         attention_mask = torch.stack(batch['attention_mask']).transpose(0, 1).to(device)
    #         start_positions = batch['start_positions'].clone().detach().to(device)
    #         end_positions = batch['end_positions'].clone().detach().to(device)

    #         input_ids = input_ids.to(device)
    #         attention_mask = attention_mask.to(device)
    #         start_positions = start_positions.to(device)
    #         end_positions = end_positions.to(device)

    #         with torch.no_grad():
    #             outputs = model(input_ids, attention_mask=attention_mask, start_positions=start_positions, end_positions=end_positions)
    #             start_predictions = torch.argmax(outputs.start_logits, dim=1)
    #             end_predictions = torch.argmax(outputs.end_logits, dim=1)

    #             for idx in range(len(start_positions)):
    #                 input_ids_example = input_ids[idx]

    #                 # Find the position of the second SEP token
    #                 sep_positions = (input_ids_example == tokenizer.sep_token_id).nonzero(as_tuple=True)[0]
    #                 sep_position = sep_positions[1].item()

    #                 # Decode the question text from input_ids
    #                 question = tokenizer.decode(input_ids_example[:sep_position], skip_special_tokens=True)

    #                 predicted_start = start_predictions[idx].item()
    #                 predicted_end = end_predictions[idx].item()
    #                 true_start = start_positions[idx].item()
    #                 true_end = end_positions[idx].item()

    #                 # Get the predicted answer text
    #                 predicted_answer = tokenizer.decode(input_ids_example[sep_position + predicted_start:sep_position + predicted_end + 1].tolist(), skip_special_tokens=True)

    #                 # Get the true answer text
    #                 true_answer = tokenizer.decode(input_ids_example[sep_position + true_start:sep_position + true_end + 1].tolist(), skip_special_tokens=True)

    #                 predicted_answers.append(predicted_answer)
    #                 true_answers.append(true_answer)

    #                 # logger.debug(f"[{dataset_name}] Predicted answer: {predicted_answer}")
    #                 # logger.debug(f"[{dataset_name}] True answer: {true_answer}")


    # logger.critical(f"I am here!")
    # # Save the true and predicted answers to a CSV file
    # with open("answers.csv", "w", newline='', encoding='utf-8') as csvfile:
    #     csv_writer = csv.writer(csvfile)
    #     csv_writer.writerow(["predicted_answer", "true_answer"])

    #     for predicted_answer, true_answer in zip(predicted_answers, true_answers):
    #         csv_writer.writerow([predicted_answer, true_answer])

    # # Plot the training loss per iteration, and validation and test loss per epoch
    # iterations_train = range(1, len(train_losses) + 1)
    # iterations_val = range(1, len(val_losses) + 1)
    # iterations_test = range(1, len(test_losses) + 1)

    # iterations_train_acc = range(1, len(train_accuracies) + 1)
    # iterations_val_acc = range(1, len(val_accuracies) + 1)
    # iterations_test_acc = range(1, len(test_accuracies) + 1)
    # logger.critical(f"I am here!")
    # # Train, validation, and test loss plots
    # plt.plot(train_losses, label='Training loss')
    # plt.plot(val_losses, label='Validation loss')
    # plt.plot(test_losses, label='Test loss')

    # plt.title(f'Losses (lr={lr}, num_epochs={num_epochs})')
    # plt.xlabel('Iterations')
    # plt.ylabel('Loss')
    # plt.legend()

    # plt.savefig(f'loss_plot_QA_{num_epochs}_{lr}.png')
    # plt.show()
    # plt.close()

    # # Train, validation, and test exact match plots
    # plt.plot(train_exact_matches, label='Train exact match')
    # plt.plot(val_exact_matches, label='Validation exact match')
    # plt.plot(test_exact_matches, label='Test exact match')

    # plt.title(f'Exact Match (lr={lr}, num_epochs={num_epochs})')
    # plt.xlabel('Iterations')
    # plt.ylabel('Exact Match')
    # plt.legend()

    # plt.savefig(f'exact_match_plot_QA_{num_epochs}_{lr}.png')
    # plt.show()
    # plt.close()
    
    # logger.critical(f"I am here!")
    # # Train, validation, and test F1 score plots
    # plt.plot(train_f1_scores, label='Train F1 score')
    # plt.plot(val_f1_scores, label='Validation F1 score')
    # plt.plot(test_f1_scores, label='Test F1 score')

    # plt.title(f'F1 Score (lr={lr}, num_epochs={num_epochs})')
    # plt.xlabel('Iterations')
    # plt.ylabel('F1 Score')
    # plt.legend()

    # plt.savefig(f'f1_score_plot_QA_{num_epochs}_{lr}.png')
    # plt.show()
    # plt.close()
