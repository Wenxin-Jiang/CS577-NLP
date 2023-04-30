from datasets import load_dataset, Dataset, concatenate_datasets
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, TrainingArguments, Trainer, BertForQuestionAnswering, AdamW, BertTokenizerFast
import numpy as np
import torch
from torch.utils.data import DataLoader

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


if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    dataset = load_dataset("json", data_files={"train": "/depot/davisjam/data/wenxin/CS577-NLP/project/squad_format_data.json", "val": "/depot/davisjam/data/wenxin/CS577-NLP/project/squad_format_data.json"}, field="data")


    # model_checkpoint = "bert-base-uncased"
    model_checkpoint = "deepset/bert-base-cased-squad2"
    # tokenizer = BertTokenizerFast.from_pretrained(model_checkpoint)
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

    # Extract questions, contexts, and answers
    questions, contexts, answers = [], [], []
    for split in ["train", "val"]:
        questions, contexts, answers = [], [], []
        for i in range(len(dataset[split])):
            paragraphs = dataset[split][i]["paragraphs"]
            for paragraph in paragraphs:
                qas = paragraph["qas"]
                context = paragraph["context"]

                for qa in qas:
                    question = qa["question"]
                    answer_text = qa["answers"][0]["text"]
                    answer_start = qa["answers"][0]["answer_start"]

                    questions.append(question)
                    contexts.append(context)
                    answers.append({"text": answer_text, "answer_start": answer_start})


        tokenized_questions = tokenizer(questions, padding="max_length", truncation=True, max_length=512, return_tensors="pt")
        tokenized_contexts = tokenizer(contexts, padding="max_length", truncation=True, max_length=512, return_tensors="pt")
        
        max_length = 512
        min_length = min(len(tokenized_questions["input_ids"]), len(tokenized_contexts["input_ids"]))

        # Combine tokenized_questions and tokenized_contexts
        tokenized_examples = {k: [] for k in tokenized_questions}
        for i in range(min_length):
            input_ids = torch.cat((tokenized_questions["input_ids"][i], tokenized_contexts["input_ids"][i]))
            attention_mask = torch.cat((tokenized_questions["attention_mask"][i], tokenized_contexts["attention_mask"][i]))
            token_type_ids = torch.cat((tokenized_questions["token_type_ids"][i], torch.tensor([1] * len(tokenized_contexts["token_type_ids"][i]), dtype=torch.long)))

            # Truncate or pad input_ids, attention_mask, and token_type_ids
            if len(input_ids) > max_length:
                input_ids = input_ids[:max_length]
                attention_mask = attention_mask[:max_length]
                token_type_ids = token_type_ids[:max_length]
            else:
                pad_length = max_length - len(input_ids)
                input_ids = torch.cat((input_ids, torch.zeros(pad_length, dtype=torch.long)))
                attention_mask = torch.cat((attention_mask, torch.zeros(pad_length, dtype=torch.long)))
                token_type_ids = torch.cat((token_type_ids, torch.zeros(pad_length, dtype=torch.long)))

            tokenized_examples["input_ids"].append(input_ids)
            tokenized_examples["attention_mask"].append(attention_mask)
            tokenized_examples["token_type_ids"].append(token_type_ids)

        # Convert lists to tensors
        for k in tokenized_examples:
            tokenized_examples[k] = torch.stack(tokenized_examples[k])




        # for k in tokenized_questions:
        #     tokenized_examples[k] = torch.cat((tokenized_questions[k], tokenized_contexts[k]), dim=1).tolist()

        answers = [a for a in answers if a["answer_start"] < max_length]

        start_positions, end_positions = [], []
        for answer in answers:
            start_positions.append(answer["answer_start"])
            end_positions.append(answer["answer_start"] + len(answer["text"]) - 1)

        tokenized_examples["start_positions"] = start_positions
        tokenized_examples["end_positions"] = end_positions

        if split == "train":
            tokenized_dataset_train = Dataset.from_dict(tokenized_examples)
        elif split == "val":
            tokenized_dataset_val = Dataset.from_dict(tokenized_examples)

    model = BertForQuestionAnswering.from_pretrained(model_checkpoint)
    # If need to load model from checkpoint
    # model.load_state_dict(torch.load("model_epoch_1.pt"))  # Replace "model_epoch_1.pt" with the appropriate filename
    model = model.to(device)

    train_loader = DataLoader(tokenized_dataset_train, batch_size=2, shuffle=True)
    eval_loader = DataLoader(tokenized_dataset_val, batch_size=2, shuffle=True)

    optimizer = AdamW(model.parameters(), lr=2e-5)

    for epoch in range(3):
        model.train()
        train_loss = 0
        for i, batch in enumerate(train_loader):
            input_ids = torch.stack(batch['input_ids']).transpose(0, 1)
            attention_mask = torch.stack(batch['attention_mask']).transpose(0, 1)
            start_positions = batch['start_positions'].view(-1)
            end_positions = batch['end_positions'].view(-1)
            if i == 0:
                logger.critical(f"Using device: {device}")
                logger.debug(f"input_ids: {input_ids.shape}, start_positions: {start_positions.shape}, end_positions: {end_positions.shape}")
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
        torch.save(model.state_dict(), f"QA_SmallModel_epoch_{epoch+1}.pt")


    # # Define training arguments
    # training_args = TrainingArguments(
    #     output_dir='./results',          # output directory
    #     num_train_epochs=3,              # total number of training epochs
    #     per_device_train_batch_size=16,  # batch size per device during training
    #     per_device_eval_batch_size=64,   # batch size for evaluation
    #     warmup_steps=500,                # number of warmup steps for learning rate scheduler
    #     weight_decay=0.01,               # strength of weight decay
    #     logging_dir='./logs',            # directory for storing logs
    #     logging_steps=10,
    # )

    # # Define trainer
    # trainer = Trainer(
    #     model=model,
    #     args=training_args,
    #     train_dataset=tokenized_dataset_train,
    #     eval_dataset=tokenized_dataset_val,
    #     tokenizer = tokenizer,
    #     compute_loss=compute_loss,
    # )

    # # TODO: add loss function

    # # Train the model
    # trainer.train()

    # # Evaluate the model
    # trainer.evaluate()