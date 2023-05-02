---
license: mit
tags:
- generated_from_trainer
model-index:
- name: roberta-tapt-acl-arc
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-tapt-acl-arc

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3472

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
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 89   | 2.6476          |
| No log        | 2.0   | 178  | 2.7191          |
| No log        | 3.0   | 267  | 2.4195          |
| No log        | 4.0   | 356  | 2.4680          |
| No log        | 5.0   | 445  | 2.3363          |
| 2.5791        | 6.0   | 534  | 2.1846          |
| 2.5791        | 7.0   | 623  | 2.0593          |
| 2.5791        | 8.0   | 712  | 1.9373          |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
