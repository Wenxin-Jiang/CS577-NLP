---
tags:
- generated_from_trainer
datasets:
- becasv2
model-index:
- name: legalectra-small-spanish-becasv3-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# legalectra-small-spanish-becasv3-1

This model is a fine-tuned version of [mrm8488/legalectra-small-spanish](https://huggingface.co/mrm8488/legalectra-small-spanish) on the becasv2 dataset.
It achieves the following results on the evaluation set:
- Loss: 5.5694

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
- train_batch_size: 10
- eval_batch_size: 10
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 8    | 5.8980          |
| No log        | 2.0   | 16   | 5.8136          |
| No log        | 3.0   | 24   | 5.7452          |
| No log        | 4.0   | 32   | 5.6940          |
| No log        | 5.0   | 40   | 5.6554          |
| No log        | 6.0   | 48   | 5.6241          |
| No log        | 7.0   | 56   | 5.5997          |
| No log        | 8.0   | 64   | 5.5830          |
| No log        | 9.0   | 72   | 5.5730          |
| No log        | 10.0  | 80   | 5.5694          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
