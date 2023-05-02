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
- name: mbert-hate-final-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbert-hate-final-1

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6751
- Accuracy: 0.7272
- Precision: 0.7260
- Recall: 0.7272
- F1: 0.7188

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
| No log        | 1.0   | 296  | 0.5531          | 0.6835   | 0.6803    | 0.6835 | 0.6812 |
| 0.5365        | 2.0   | 592  | 0.5304          | 0.7405   | 0.7432    | 0.7405 | 0.7302 |
| 0.5365        | 3.0   | 888  | 0.5526          | 0.7310   | 0.7334    | 0.7310 | 0.7195 |
| 0.4318        | 4.0   | 1184 | 0.6142          | 0.7186   | 0.7153    | 0.7186 | 0.7136 |
| 0.4318        | 5.0   | 1480 | 0.6420          | 0.7243   | 0.7227    | 0.7243 | 0.7162 |
| 0.3507        | 6.0   | 1776 | 0.6751          | 0.7272   | 0.7260    | 0.7272 | 0.7188 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
