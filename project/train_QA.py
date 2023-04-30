import torch
import random
import json
import csv
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader
from datasets import load_dataset, Dataset, concatenate_datasets
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, TrainingArguments, Trainer, BertForQuestionAnswering, AdamW, BertTokenizerFast
from collections import Counter
from sklearn.metrics import f1_score

import os
os.environ["WANDB_DISABLED"] = "true"


from loguru import logger


class QAModel(AutoModelForQuestionAnswering):
    def forward(self, input_ids, attention_mask=None, token_type_ids=None, start_positions=None, end_positions=None):
        outputs = self.bert(input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)

        sequence_output = outputs[0]
        logits = self.qa_outputs(sequence_output)
        start_logits, end_logits = logits.split(1, dim=-1)
        start_logits = start_logits.squeeze(-1)
        end_logits = end_logits.squeeze(-1)

        loss = None
        if start_positions is not None and end_positions is not None:
            # If we are on multi-GPU, split add a dimension
            if len(start_positions.size()) > 1:
                start_positions = start_positions.squeeze(-1)
            if len(end_positions.size()) > 1:
                end_positions = end_positions.squeeze(-1)

            # sometimes the start/end positions are outside our model inputs, we ignore these terms
            ignored_index = start_logits.size(1)
            start_positions.clamp_(0, ignored_index)
            end_positions.clamp_(0, ignored_index)

            loss_fct = torch.nn.CrossEntropyLoss(ignore_index=ignored_index)
            start_loss = loss_fct(start_logits, start_positions)
            end_loss = loss_fct(end_logits, end_positions)
            loss = (start_loss + end_loss) / 2

        return (start_logits, end_logits, loss)


def compute_loss(model, inputs):
    outputs = model(input_ids=inputs['input_ids'], attention_mask=inputs['attention_mask'], token_type_ids=inputs['token_type_ids'], start_positions=inputs['start_positions'], end_positions=inputs['end_positions'])
    return outputs[2]


# Extract questions, contexts, and answers
def process_dataset(split_dataset, split):
    examples = []

    for i in range(len(split_dataset)):
        paragraphs = split_dataset[i]["paragraphs"]
        for paragraph in paragraphs:
            qas = paragraph["qas"]
            context = paragraph["context"]

            for qa in qas:
                question = qa["question"]
                answer_text = qa["answers"][0]["text"]
                answer_start = qa["answers"][0]["answer_start"]

                examples.append({"question": question, "context": context, "answer": {"text": answer_text, "answer_start": answer_start}})

    tokenized_examples = {
        "input_ids": [],
        "attention_mask": [],
        "token_type_ids": [],
        "start_positions": [],
        "end_positions": [],
    }

    for example in examples:
        question = example["question"]
        context = example["context"]
        answer = example["answer"]

        tokenized_input = tokenizer(question, context, padding="max_length", truncation=True, max_length=512, return_tensors="pt")

        input_ids = tokenized_input["input_ids"][0]
        attention_mask = tokenized_input["attention_mask"][0]
        token_type_ids = tokenized_input["token_type_ids"][0]

        answer_start = max(0, answer["answer_start"])
        answer_start_token_index = tokenized_input.char_to_token(answer_start)
        answer_end_token_index = tokenized_input.char_to_token(answer["answer_start"] + len(answer["text"]) - 1)

        if answer_start_token_index is not None and answer_end_token_index is not None:
            tokenized_examples["input_ids"].append(input_ids)
            tokenized_examples["attention_mask"].append(attention_mask)
            tokenized_examples["token_type_ids"].append(token_type_ids)
            tokenized_examples["start_positions"].append(answer_start_token_index)
            tokenized_examples["end_positions"].append(answer_end_token_index)

    # Convert lists to tensors
    for k in tokenized_examples:
        if k in ["start_positions", "end_positions"]:
            tokenized_examples[k] = torch.tensor(tokenized_examples[k], dtype=torch.long)
        else:
            tokenized_examples[k] = torch.stack(tokenized_examples[k])

    return tokenized_examples





def compute_accuracy(predictions, start_positions, end_positions):
    correct = 0
    total = len(predictions)

    for pred, true_start, true_end in zip(predictions, start_positions, end_positions):
        if pred["start"] == true_start and pred["end"] == true_end:
            correct += 1

    accuracy = correct / total
    return accuracy

def evaluate(model, loader):
    model.eval()
    predictions = []
    true_labels = []
    correct = 0
    total = 0

    with torch.no_grad():
        for batch in loader:
            input_ids = torch.stack(batch['input_ids']).transpose(0, 1)
            attention_mask = torch.stack(batch['attention_mask']).transpose(0, 1)
            start_positions = batch['start_positions'].view(-1)
            end_positions = batch['end_positions'].view(-1)

            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)
            start_positions = start_positions.to(device)
            end_positions = end_positions.to(device)

            outputs = model(input_ids, attention_mask=attention_mask)
            start_logits, end_logits = outputs["start_logits"], outputs["end_logits"]


            # logger.debug(f"start_logits: {start_logits}")
            # logger.debug(f"end_logits: {end_logits}")

            start_preds = torch.argmax(start_logits, dim=1)
            end_preds = torch.argmax(end_logits, dim=1)

            predictions.extend(zip(start_preds.tolist(), end_preds.tolist()))
            true_labels.extend(zip(start_positions.tolist(), end_positions.tolist()))

            correct += ((start_preds == start_positions) & (end_preds == end_positions)).sum().item()
            total += len(start_positions)

    accuracy = correct / total
    return predictions, true_labels, accuracy


def generate_predicted_answers(data, predictions):
    predicted_answers = []
    for paragraph in data["data"][0]["paragraphs"]:
        for i, qa in enumerate(paragraph["qas"]):
            start_pred, end_pred = predictions[i]
            context = paragraph["context"]
            predicted_answer = context[start_pred:end_pred+1]
            predicted_answers.append(predicted_answer)
    return predicted_answers


def compute_metrics(true_start, true_end, start_pred, end_pred):
    true = set(range(true_start, true_end+1))
    pred = set(range(start_pred, end_pred+1))

    common = true.intersection(pred)
    if len(common) == 0:
        return 0, 0

    precision = len(common) / len(pred)
    recall = len(common) / len(true)

    f1 = 2 * (precision * recall) / (precision + recall)
    exact_match = int(true_start == start_pred and true_end == end_pred)

    return exact_match, f1


def positions_to_text(input_ids, tokenizer, start_position, end_position):
    tokens = input_ids[start_position: end_position + 1]
    text = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(tokens))
    return text



if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # raw_dataset = load_dataset("json", data_files={"train": "/depot/davisjam/data/wenxin/CS577-NLP/project/squad_format_data.json", "val": "/depot/davisjam/data/wenxin/CS577-NLP/project/squad_format_data.json"}, field="data")
    with open("/depot/davisjam/data/wenxin/CS577-NLP/project/squad_format_data.json", "r") as f:
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

    
        
    tokenized_train = process_dataset(train_dataset, "train")
    tokenized_val = process_dataset(val_dataset, "val")
    tokenized_test = process_dataset(test_dataset, "test")

    # Convert dictionaries to Datasets
    tokenized_dataset_train = Dataset.from_dict(tokenized_train)
    tokenized_dataset_val = Dataset.from_dict(tokenized_val)
    tokenized_dataset_test = Dataset.from_dict(tokenized_test)

    model = BertForQuestionAnswering.from_pretrained(model_checkpoint)
    # If need to load model from checkpoint
    # model.load_state_dict(torch.load("model_epoch_1.pt"))  # Replace "model_epoch_1.pt" with the appropriate filename
    model = model.to(device)

    batch_size = 16
    train_loader = DataLoader(tokenized_dataset_train, batch_size=batch_size, shuffle=True)
    eval_loader = DataLoader(tokenized_dataset_val, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(tokenized_dataset_test, batch_size=batch_size, shuffle=True)
    lr = 2e-6
    num_epochs = 2
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
            input_ids = torch.stack(batch['input_ids']).transpose(0, 1)
            attention_mask = torch.stack(batch['attention_mask']).transpose(0, 1)
            start_positions = batch['start_positions'].view(-1)
            end_positions = batch['end_positions'].view(-1)
            if i == 0:
                logger.critical(f"Using device: {device}")
                # logger.debug(f"input_ids: {input_ids.shape}, start_positions: {start_positions.shape}, end_positions: {end_positions.shape}")
            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)
            start_positions = start_positions.to(device)
            end_positions = end_positions.to(device)
            optimizer.zero_grad()
            outputs = model(input_ids, attention_mask=attention_mask, start_positions=start_positions, end_positions=end_positions)
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            train_loss += loss.item()
            train_losses.append(loss.item())
            # if i % 10 == 0:
            logger.info(f"Epoch {epoch+1}, Batch {i+1} - Loss: {loss.item():.4f}")
        
        
        avg_train_loss = train_loss / len(train_loader)
        
        model.eval()
        eval_loss = 0
        for i, batch in enumerate(eval_loader):
            input_ids = torch.stack(batch['input_ids']).transpose(0, 1)
            attention_mask = torch.stack(batch['attention_mask']).transpose(0, 1)
            start_positions = batch['start_positions'].view(-1)
            end_positions = batch['end_positions'].view(-1)

            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)
            start_positions = start_positions.to(device)
            end_positions = end_positions.to(device)
            
            with torch.no_grad():
                outputs = model(input_ids, attention_mask=attention_mask, start_positions=start_positions, end_positions=end_positions)
                loss = outputs.loss
                eval_loss += loss.item()

        avg_eval_loss = eval_loss / len(eval_loader)

        logger.critical(f"Epoch {epoch+1} - Train loss: {avg_train_loss:.4f} - Eval loss: {avg_eval_loss:.4f}")
        torch.save(model.state_dict(), f"QA_BERT_epoch_{epoch+1}.pt")


        exact_matches = []
        f1_scores = []
        
        # Test loop
        model.eval()
        test_loss = 0
        for i, batch in enumerate(test_loader):
            input_ids = torch.stack(batch['input_ids']).transpose(0, 1)
            attention_mask = torch.stack(batch['attention_mask']).transpose(0, 1)
            start_positions = batch['start_positions'].view(-1)
            end_positions = batch['end_positions'].view(-1)

            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)
            start_positions = start_positions.to(device)
            end_positions = end_positions.to(device)

            with torch.no_grad():
                outputs = model(input_ids, attention_mask=attention_mask, start_positions=start_positions, end_positions=end_positions)
                loss = outputs.loss
                test_loss += loss.item()
                val_losses.append(loss.item())
                
                start_predictions = torch.argmax(outputs.start_logits, dim=1)
                end_predictions = torch.argmax(outputs.end_logits, dim=1)

                for start_pred, end_pred, true_start, true_end in zip(start_predictions, end_predictions, start_positions, end_positions):
                    # logger.debug(f"start_pred: {start_pred}, end_pred: {end_pred}, true_start: {true_start}, true_end: {true_end}")
                    exact_match, f1 = compute_metrics(true_start.item(), true_end.item(), start_pred.item(), end_pred.item())
                    # logger.debug(f"Exact match: {exact_match}, F1: {f1}")
                    exact_matches.append(exact_match)
                    f1_scores.append(f1)

        exact_match_percentage = sum(exact_matches) / len(exact_matches) * 100
        f1_average = sum(f1_scores) / len(f1_scores)

        logger.critical(f"Exact Match Percentage: {exact_match_percentage}")
        logger.critical(f"Average F1 Score: {f1_average}")

        
        avg_test_loss = test_loss / len(test_loader)
        logger.critical(f"Test loss: {avg_test_loss:.4f}")
        
        test_losses.append(avg_test_loss)
    
        train_predictions, train_true_labels, train_accuracy = evaluate(model, train_loader)
        val_predictions, val_true_labels, val_accuracy = evaluate(model, eval_loader)
        test_predictions, test_true_labels, test_accuracy = evaluate(model, test_loader)

        logger.info(f"Train accuracy: {train_accuracy:.4f}")
        logger.info(f"Val accuracy: {val_accuracy:.4f}")
        logger.info(f"Test accuracy: {test_accuracy:.4f}")
        train_accuracies.append(train_accuracy)
        val_accuracies.append(val_accuracy)
        test_accuracies.append(test_accuracy)

    with open("train_predictions.csv", "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["start_pred", "end_pred", "true_start", "true_end"])
        for pred, true_label in zip(train_predictions, train_true_labels):
            csv_writer.writerow([pred[0], pred[1], true_label[0], true_label[1]])

    with open("val_predictions.csv", "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["start_pred", "end_pred", "true_start", "true_end"])
        for pred, true_label in zip(val_predictions, val_true_labels):
            csv_writer.writerow([pred[0], pred[1], true_label[0], true_label[1]])
    
    with open("test_predictions.csv", "w", newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["start_pred", "end_pred", "true_start", "true_end"])
            for pred, true_label in zip(test_predictions, test_true_labels):
                csv_writer.writerow([pred[0], pred[1], true_label[0], true_label[1]])
    
    input_texts = []  # Store the original input texts
    predicted_texts = []
    true_texts = []

    for i, batch in enumerate(test_loader):
        input_ids = torch.stack(batch['input_ids']).transpose(0, 1)
        
        for j in range(input_ids.size(1)):
            # input_text = positions_to_text(input_ids[:, j], tokenizer, 1, input_ids[:, j].tolist().index(tokenizer.sep_token_id) - 1)
            input_ids_list = input_ids[:, j].tolist()
            if tokenizer.sep_token_id in input_ids_list:
                end_index = input_ids_list.index(tokenizer.sep_token_id) - 1
            else:
                end_index = len(input_ids_list) - 1
            input_text = positions_to_text(input_ids[:, j], tokenizer, 1, end_index)

            predicted_text = positions_to_text(input_ids[:, j], tokenizer, test_predictions[i * test_loader.batch_size + j][0], test_predictions[i * test_loader.batch_size + j][1])
            true_text = positions_to_text(input_ids[:, j], tokenizer, test_true_labels[i * test_loader.batch_size + j][0], test_true_labels[i * test_loader.batch_size + j][1])

            input_texts.append(input_text)
            predicted_texts.append(predicted_text)
            true_texts.append(true_text)

    with open("text_predictions.csv", "w", newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["input_text", "predicted_text", "true_text"])

        for input_text, predicted_text, true_text in zip(input_texts, predicted_texts, true_texts):
            csv_writer.writerow([input_text, predicted_text, true_text])

    # Plot the training loss per iteration, and validation and test loss per epoch
    iterations_train = range(1, len(train_losses) + 1)
    iterations_val = range(1, len(val_losses) + 1)
    iterations_test = range(1, len(test_losses) + 1)

    plt.plot(iterations_train, train_losses, 'b', label='Training loss')
    
    plt.title(f'Training  Loss, lr={lr}')
    plt.xlabel('Iterations')
    plt.ylabel('Loss')

    # Save the plot to a file
    plt.savefig(f'loss_plot_QA_{lr}_train.png')
    plt.show()
    plt.close()

    plt.plot(iterations_val, val_losses, 'r', label='Validation loss')
    plt.plot(iterations_test, test_losses, 'r', label='Validation loss')
    plt.title(f'Validation and Test  Loss, lr={lr}')
    plt.xlabel('Iterations')
    plt.ylabel('Loss')

    # Save the plot to a file
    plt.savefig(f'loss_plot_QA_{lr}_val+test.png')
    plt.show()
    plt.close()

    # TODO: More evaluations 