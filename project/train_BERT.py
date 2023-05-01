import os
os.environ["WANDB_DISABLED"] = "true"

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from transformers import AutoTokenizer, AutoModelForSequenceClassification, \
    TrainingArguments, Trainer, DataCollatorWithPadding, BertForSequenceClassification
from transformers.modeling_outputs import SequenceClassifierOutput

import matplotlib.pyplot as plt
from datasets import Dataset
from typing import List, Dict, Union
import torch
from torch.utils.data import Dataset as TorchDataset
from torch.nn import BCEWithLogitsLoss, MSELoss

import numpy as np
import argparse

from loguru import logger

def parse_arguments():
    parser = argparse.ArgumentParser(description="Fine-tune a BERT model for information extraction on README files")
    parser.add_argument("--test_only", action="store_true", help="Test the model without training")

    return parser.parse_args()


def custom_collate(batch):
    max_len = max([x["input_ids"].shape[0] for x in batch])
    input_ids = torch.stack([torch.cat([x["input_ids"], torch.zeros(max_len - x["input_ids"].shape[0], dtype=torch.long)]) for x in batch])
    attention_mask = torch.stack([torch.cat([x["attention_mask"], torch.zeros(max_len - x["attention_mask"].shape[0], dtype=torch.long)]) for x in batch])
    labels = torch.stack([x["labels"] for x in batch])

    return {"input_ids": input_ids, "attention_mask": attention_mask, "labels": labels}



class CustomDataset(TorchDataset):
    def __init__(self, df, tokenizer):
        self.df = df
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        example = self.df.iloc[idx].to_dict()
        # logger.debug(example)
        inputs = self.tokenizer(example["readme_text"], padding=True, truncation=True, return_tensors="pt")
        return {
            "input_ids": inputs["input_ids"].squeeze(0),
            "attention_mask": inputs["attention_mask"].squeeze(0),
            "labels": torch.tensor(example["label"], dtype=torch.long)
        }


class BertForMultiLabelSequenceClassification(BertForSequenceClassification):
    def __init__(self, config):
        super().__init__(config)

    def forward(
        self,
        input_ids=None,
        attention_mask=None,
        token_type_ids=None,
        position_ids=None,
        head_mask=None,
        inputs_embeds=None,
        labels=None,
        output_attentions=None,
        output_hidden_states=None,
        return_dict=None,
    ):
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict

        outputs = self.bert(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            position_ids=position_ids,
            head_mask=head_mask,
            inputs_embeds=inputs_embeds,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )
        # logger.debug(f"outputs: {outputs}")
        pooled_output = outputs[1]

        pooled_output = self.dropout(pooled_output)
        logits = self.classifier(pooled_output)

        loss = None
        if labels is not None:
            if self.num_labels == 1:
                # We are doing regression
                loss_fct = MSELoss()
                loss = loss_fct(logits.view(-1), labels.view(-1))
            else:
                # logger.debug(f"logits for BCEWithLogitsLoss: {logits}")
                # logger.debug(f"labels for BCEWithLogitsLoss: {labels}")
                loss_fct = BCEWithLogitsLoss()
                loss = loss_fct(logits, labels.float())

        if not return_dict:
            logger.debug(f"return_dict: {return_dict}")
            output = (logits,) + outputs[2:]
            return ((loss,) + output) if loss is not None else output

        # logger.debug(f"outputs.hidden_states: {outputs.hidden_states}")
        # logger.debug(f"outputs.attentions: {outputs.attentions}")
        # exit(-1)
        return SequenceClassifierOutput(
            loss=loss,
            logits=logits,
            hidden_states=outputs.hidden_states,
            attentions=outputs.attentions,
        )


def compute_metrics(pred):
    # Extract true labels and predicted labels from the prediction object
    labels = pred.label_ids
    preds = np.where(pred.predictions > 0.5, 1, 0)

    # Compute accuracy, F1 score, precision, and recall
    acc = accuracy_score(labels, preds)
    f1 = f1_score(labels, preds, average='weighted', zero_division=1)
    precision = precision_score(labels, preds, average='weighted', zero_division=1)
    recall = recall_score(labels, preds, average='weighted', zero_division=1)

    # Create a dictionary of the computed metrics
    metrics = {
        'accuracy': acc,
        'f1': f1,
        'precision': precision,
        'recall': recall
    }

    # Print the metrics to the console for debugging
    print("Computed metrics:", metrics)

    return metrics


def plot_learning_curve(losses, metric_values, metric_name, epoch):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(losses, label="Loss")
    plt.xlabel("Steps")
    plt.ylabel("Loss")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(metric_values, label=metric_name)
    plt.xlabel("Steps")
    plt.ylabel(metric_name)
    plt.legend()

    plt.savefig(f"learning_curve_Epoch{epoch}.jpg")




def print_predicted_metadata(predictions, label_map_inverse, threshold=0.4):
    for i, pred in enumerate(predictions):
        pred_labels = np.where(pred > threshold, 1, 0)
        pred_metadata = [label_map_inverse[label_idx] for label_idx, is_present in enumerate(pred_labels) if is_present]

        logger.info(f"Example {i + 1}:")
        logger.info(f"Predicted metadata: {pred_metadata}")
        print("\n")


def new_func(predictions):
    logger.debug(predictions)


if __name__ == "__main__":
    args = parse_arguments()

    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

    # Load the training data
    df = pd.read_csv("/depot/davisjam/data/wenxin/CS577-NLP/project/metadata_train_withREADME.csv")

    # Clean None readme_text
    df.replace("None", None, inplace=True)
    df.dropna(subset=['readme_text'], inplace=True)

    # Define the labels
    labels = ['model_architecture', 'model_task', 'model_category']
    label_values = [df[label].unique().tolist() for label in labels]
    label_map = {label: i for i, label in enumerate(sum(label_values, []))}
    label_map_inverse = {v: k for k, v in label_map.items()}
    
    # One-hot encode labels
    mlb = MultiLabelBinarizer(classes=list(label_map.values()))
    df['label'] = df[labels].apply(lambda x: mlb.fit_transform([[label_map[y] for y in x]])[0], axis=1)

    # Split the data into training, validation, and testing sets
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=123)
    train_df, valid_df = train_test_split(train_df, test_size=0.2, random_state=123)


    

    # Load the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

    if args.test_only:
        # TODO: Check if this works for loading the model
        model_path = "./results/checkpoint-2000"
        model = torch.load(model_path)

    else:
        model_path = "bert-base-uncased" 

        model = BertForMultiLabelSequenceClassification.from_pretrained(model_path, num_labels=len(label_map))
        
    model = model.to(device)

    training_args = TrainingArguments(
        output_dir='./results/epoch5',
        num_train_epochs=3,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=64,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='./logs_epoch5_GPU',
        logging_steps=50,
        evaluation_strategy='steps',
        save_strategy='steps',
        save_steps=500,
        load_best_model_at_end=True,
        metric_for_best_model='accuracy',
        greater_is_better=True,
        eval_steps=500,
        fp16=True, # Use mixed precision training
    )

    
    train_dataset = CustomDataset(train_df, tokenizer)
    valid_dataset = CustomDataset(valid_df, tokenizer)

    logger.info(f"len(train_dataset) = {len(train_dataset)}")
    logger.info(f"len(valid_dataset) = {len(valid_dataset)}")

    logger.critical(f"Training is Starting on {device}")

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=valid_dataset,
        tokenizer=tokenizer,
        compute_metrics=compute_metrics,
        # data_collator=lambda data: custom_data_collator(tokenizer, data),
    )

    if not args.test_only:

        # Train the model
        trainer.train()

    # Evaluate the model
    trainer.evaluate()

    # Plot the learning curve
    steps = [x["step"] for x in trainer.state.log_history if "loss" in x]
    losses = [x["loss"] for x in trainer.state.log_history if "loss" in x]
    metric_name = "accuracy"
    metric_values = [x[metric_name] for x in trainer.state.log_history if metric_name in x]

    plot_learning_curve(losses, metric_values, metric_name, training_args.num_train_epochs)

    # Predict metadata for a few examples from the test dataset
    test_dataset = CustomDataset(test_df, tokenizer)
    test_dataloader = torch.utils.data.DataLoader(test_dataset, batch_size=16, collate_fn=custom_collate)
    test_examples = next(iter(test_dataloader))

    with torch.no_grad():
        model.eval()
        input_ids = test_examples["input_ids"].to(device)
        attention_mask = test_examples["attention_mask"].to(device)
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        predictions = torch.sigmoid(outputs.logits).cpu().numpy()

    print_predicted_metadata(predictions, label_map_inverse)
