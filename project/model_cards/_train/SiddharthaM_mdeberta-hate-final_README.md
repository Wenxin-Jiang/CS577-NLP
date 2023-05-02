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
- name: mdeberta-hate-final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mdeberta-hate-final

This model is a fine-tuned version of [microsoft/mdeberta-v3-base](https://huggingface.co/microsoft/mdeberta-v3-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6223
- Accuracy: 0.7424
- Precision: 0.7410
- Recall: 0.7424
- F1: 0.7363

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
| No log        | 1.0   | 296  | 0.5309          | 0.7519   | 0.7685    | 0.7519 | 0.7357 |
| 0.5358        | 2.0   | 592  | 0.5228          | 0.7510   | 0.7663    | 0.7510 | 0.7351 |
| 0.5358        | 3.0   | 888  | 0.5565          | 0.7510   | 0.7513    | 0.7510 | 0.7438 |
| 0.4295        | 4.0   | 1184 | 0.5639          | 0.7481   | 0.7488    | 0.7481 | 0.7403 |
| 0.4295        | 5.0   | 1480 | 0.5941          | 0.7510   | 0.7531    | 0.7510 | 0.7423 |
| 0.3701        | 6.0   | 1776 | 0.6223          | 0.7424   | 0.7410    | 0.7424 | 0.7363 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
