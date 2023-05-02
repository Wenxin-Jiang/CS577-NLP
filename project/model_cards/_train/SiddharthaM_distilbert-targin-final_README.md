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
- name: distilbert-targin-final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-targin-final

This model is a fine-tuned version of [distilbert-base-multilingual-cased](https://huggingface.co/distilbert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6307
- Accuracy: 0.6882
- Precision: 0.6443
- Recall: 0.6384
- F1: 0.6409

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
| No log        | 1.0   | 296  | 0.5882          | 0.6854   | 0.6355    | 0.6182 | 0.6226 |
| 0.5995        | 2.0   | 592  | 0.5693          | 0.7015   | 0.6590    | 0.6019 | 0.6030 |
| 0.5995        | 3.0   | 888  | 0.5823          | 0.6882   | 0.6440    | 0.6377 | 0.6403 |
| 0.5299        | 4.0   | 1184 | 0.5968          | 0.6949   | 0.6488    | 0.6340 | 0.6386 |
| 0.5299        | 5.0   | 1480 | 0.6236          | 0.6835   | 0.6430    | 0.6436 | 0.6433 |
| 0.4698        | 6.0   | 1776 | 0.6307          | 0.6882   | 0.6443    | 0.6384 | 0.6409 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
