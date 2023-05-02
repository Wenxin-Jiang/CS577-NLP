---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- squad
model-index:
- name: Bert-test-model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Bert-test-model

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the squad dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3708

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 250  | 1.7369          |
| 2.2639        | 2.0   | 500  | 1.3940          |
| 2.2639        | 3.0   | 750  | 1.3708          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
