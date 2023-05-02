---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- becasv3
model-index:
- name: distilbert-base-uncased-becasv3-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-becasv3-1

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the becasv3 dataset.
It achieves the following results on the evaluation set:
- Loss: 3.1086

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
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 8    | 5.1063          |
| No log        | 2.0   | 16   | 4.4615          |
| No log        | 3.0   | 24   | 3.9351          |
| No log        | 4.0   | 32   | 3.5490          |
| No log        | 5.0   | 40   | 3.3299          |
| No log        | 6.0   | 48   | 3.2148          |
| No log        | 7.0   | 56   | 3.1292          |
| No log        | 8.0   | 64   | 3.1086          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
