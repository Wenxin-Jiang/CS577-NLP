---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-8-7
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-8-7

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6950
- Accuracy: 0.4618

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.7156        | 1.0   | 3    | 0.6965          | 0.25     |
| 0.6645        | 2.0   | 6    | 0.7059          | 0.25     |
| 0.6368        | 3.0   | 9    | 0.7179          | 0.25     |
| 0.5944        | 4.0   | 12   | 0.7408          | 0.25     |
| 0.5369        | 5.0   | 15   | 0.7758          | 0.25     |
| 0.449         | 6.0   | 18   | 0.8009          | 0.25     |
| 0.4352        | 7.0   | 21   | 0.8209          | 0.5      |
| 0.3462        | 8.0   | 24   | 0.8470          | 0.5      |
| 0.3028        | 9.0   | 27   | 0.8579          | 0.5      |
| 0.2365        | 10.0  | 30   | 0.8704          | 0.5      |
| 0.2023        | 11.0  | 33   | 0.8770          | 0.5      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
