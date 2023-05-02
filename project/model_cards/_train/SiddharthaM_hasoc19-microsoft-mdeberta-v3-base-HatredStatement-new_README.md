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
- name: hasoc19-microsoft-mdeberta-v3-base-HatredStatement-new
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hasoc19-microsoft-mdeberta-v3-base-HatredStatement-new

This model is a fine-tuned version of [microsoft/mdeberta-v3-base](https://huggingface.co/microsoft/mdeberta-v3-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6039
- Accuracy: 0.7329
- Precision: 0.7324
- Recall: 0.7329
- F1: 0.7316

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
| No log        | 1.0   | 296  | 0.5276          | 0.7253   | 0.7258    | 0.7253 | 0.7225 |
| 0.5406        | 2.0   | 592  | 0.5513          | 0.7319   | 0.7348    | 0.7319 | 0.7278 |
| 0.5406        | 3.0   | 888  | 0.5466          | 0.7357   | 0.7458    | 0.7357 | 0.7283 |
| 0.4372        | 4.0   | 1184 | 0.5531          | 0.7452   | 0.7502    | 0.7452 | 0.7406 |
| 0.4372        | 5.0   | 1480 | 0.5927          | 0.7367   | 0.7364    | 0.7367 | 0.7352 |
| 0.3868        | 6.0   | 1776 | 0.6039          | 0.7329   | 0.7324    | 0.7329 | 0.7316 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
