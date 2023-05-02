---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: BioLinkBERT-base-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BioLinkBERT-base-finetuned-ner

This model is a fine-tuned version of [michiyasunaga/BioLinkBERT-base](https://huggingface.co/michiyasunaga/BioLinkBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1226
- Precision: 0.8760
- Recall: 0.9185
- F1: 0.8968
- Accuracy: 0.9647

## Model description

This model is designed to perform NER function for specific text using BioLink BERT

## Intended uses & limitations

The goal was to have a drug tag printed immediately for a particular sentence, but it has the disadvantage of being marked as LABEL

LABEL0 : irrelevant text
LABEL1,2 : Drug
LABEL3,4 : condition

## Training and evaluation data

More information needed

## Training procedure

Reference Code: SciBERT Fine-Tuning on Drug/ADE Corpus (https://github.com/jsylee/personal-projects/blob/master/Hugging%20Face%20ADR%20Fine-Tuning/SciBERT%20ADR%20Fine-Tuning.ipynb) 

## How to use

from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("HMHMlee/BioLinkBERT-base-finetuned-ner")

model = AutoModelForTokenClassification.from_pretrained("HMHMlee/BioLinkBERT-base-finetuned-ner")

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1099        | 1.0   | 201  | 0.1489          | 0.8415    | 0.9032 | 0.8713 | 0.9566   |
| 0.1716        | 2.0   | 402  | 0.1318          | 0.8456    | 0.9135 | 0.8782 | 0.9597   |
| 0.1068        | 3.0   | 603  | 0.1197          | 0.8682    | 0.9110 | 0.8891 | 0.9641   |
| 0.0161        | 4.0   | 804  | 0.1219          | 0.8694    | 0.9157 | 0.8919 | 0.9639   |
| 0.1499        | 5.0   | 1005 | 0.1226          | 0.8760    | 0.9185 | 0.8968 | 0.9647   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
