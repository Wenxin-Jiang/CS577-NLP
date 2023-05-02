---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: sbi-model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sbi-model

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5290
- F1: 0.8211

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 1.813         | 1.0   | 40   | 1.5304          | 0.5227 |
| 1.2312        | 2.0   | 80   | 0.9138          | 0.7439 |
| 0.7428        | 3.0   | 120  | 0.6869          | 0.7518 |
| 0.5055        | 4.0   | 160  | 0.5766          | 0.8050 |
| 0.3581        | 5.0   | 200  | 0.5454          | 0.8052 |
| 0.2664        | 6.0   | 240  | 0.5208          | 0.8200 |
| 0.2145        | 7.0   | 280  | 0.5218          | 0.8241 |
| 0.1853        | 8.0   | 320  | 0.5290          | 0.8211 |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Tokenizers 0.12.1
