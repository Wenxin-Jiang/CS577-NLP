---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-small-tuto-mt5-small-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-small-tuto-mt5-small-2

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8564
- Rouge1: 0.4159
- Rouge2: 0.2906
- Rougel: 0.3928
- Rougelsum: 0.3929

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:------:|:---------:|
| 2.1519        | 1.0   | 6034  | 1.8564          | 0.4159 | 0.2906 | 0.3928 | 0.3929    |
| 2.1289        | 2.0   | 12068 | 1.8564          | 0.4159 | 0.2906 | 0.3928 | 0.3929    |
| 2.1291        | 3.0   | 18102 | 1.8564          | 0.4159 | 0.2906 | 0.3928 | 0.3929    |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
