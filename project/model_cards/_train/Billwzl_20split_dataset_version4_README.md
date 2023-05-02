---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: 20split_dataset_version4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 20split_dataset_version4

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.1060

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 16

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 3.4213        | 1.0   | 313  | 3.2276          |
| 3.2295        | 2.0   | 626  | 3.2054          |
| 3.0262        | 3.0   | 939  | 3.1718          |
| 2.9608        | 4.0   | 1252 | 3.1649          |
| 2.8715        | 5.0   | 1565 | 3.1499          |
| 2.7614        | 6.0   | 1878 | 3.1471          |
| 2.6688        | 7.0   | 2191 | 3.1280          |
| 2.6582        | 8.0   | 2504 | 3.1348          |
| 2.5296        | 9.0   | 2817 | 3.1149          |
| 2.5086        | 10.0  | 3130 | 3.1200          |
| 2.4567        | 11.0  | 3443 | 3.1020          |
| 2.4052        | 12.0  | 3756 | 3.1257          |
| 2.3513        | 13.0  | 4069 | 3.1222          |
| 2.3561        | 14.0  | 4382 | 3.1102          |
| 2.3574        | 15.0  | 4695 | 3.1027          |
| 2.3192        | 16.0  | 5008 | 3.1060          |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
