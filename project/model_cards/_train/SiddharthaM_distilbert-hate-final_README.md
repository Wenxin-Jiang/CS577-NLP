---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: distilbert-hate-final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-hate-final

This model is a fine-tuned version of [distilbert-base-multilingual-cased](https://huggingface.co/distilbert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6212
- Accuracy: 0.7253
- Precision: 0.7207
- Recall: 0.7253
- F1: 0.7206

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 1.0   | 296  | 0.5760          | 0.7025   | 0.7053    | 0.7025 | 0.6771 |
| 0.569         | 2.0   | 592  | 0.5629          | 0.7215   | 0.7168    | 0.7215 | 0.7122 |
| 0.569         | 3.0   | 888  | 0.5616          | 0.7310   | 0.7274    | 0.7310 | 0.7215 |
| 0.4683        | 4.0   | 1184 | 0.5651          | 0.7338   | 0.7295    | 0.7338 | 0.7274 |
| 0.4683        | 5.0   | 1480 | 0.5898          | 0.7338   | 0.7305    | 0.7338 | 0.7246 |
| 0.4086        | 6.0   | 1776 | 0.6212          | 0.7253   | 0.7207    | 0.7253 | 0.7206 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
