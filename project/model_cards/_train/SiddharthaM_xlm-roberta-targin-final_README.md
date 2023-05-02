---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: xlm-roberta-targin-final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-targin-final

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8172
- Accuracy: 0.6873
- Precision: 0.6494
- Recall: 0.6422
- F1: 0.6450

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 1.0   | 296  | 0.6065          | 0.6873   | 0.6537    | 0.5833 | 0.5748 |
| 0.597         | 2.0   | 592  | 0.5822          | 0.7015   | 0.6652    | 0.6279 | 0.6332 |
| 0.597         | 3.0   | 888  | 0.5704          | 0.7015   | 0.6654    | 0.6551 | 0.6589 |
| 0.5156        | 4.0   | 1184 | 0.6393          | 0.7044   | 0.6684    | 0.6552 | 0.6597 |
| 0.5156        | 5.0   | 1480 | 0.5924          | 0.7082   | 0.6752    | 0.6720 | 0.6735 |
| 0.4479        | 6.0   | 1776 | 0.7029          | 0.7006   | 0.6629    | 0.6351 | 0.6408 |
| 0.3783        | 7.0   | 2072 | 0.6963          | 0.7072   | 0.6715    | 0.6554 | 0.6606 |
| 0.3783        | 8.0   | 2368 | 0.7636          | 0.6987   | 0.6627    | 0.6549 | 0.6579 |
| 0.3253        | 9.0   | 2664 | 0.7804          | 0.6901   | 0.6549    | 0.6523 | 0.6535 |
| 0.3253        | 10.0  | 2960 | 0.8172          | 0.6873   | 0.6494    | 0.6422 | 0.6450 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
