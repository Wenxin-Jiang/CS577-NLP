---
license: apache-2.0
tags:
- Poet
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-small-ibn-Shaddad-v4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-small-ibn-Shaddad-v4

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.9233
- Rouge1: 0.0
- Rouge2: 0.0
- Rougel: 0.0
- Rougelsum: 0.0

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| 5.0001        | 1.0   | 935  | 3.1102          | 0.0    | 0.0    | 0.0    | 0.0       |
| 3.4066        | 2.0   | 1870 | 2.9836          | 0.0    | 0.0    | 0.0    | 0.0       |
| 3.2832        | 3.0   | 2805 | 2.9384          | 0.0    | 0.0    | 0.0    | 0.0       |
| 3.2334        | 4.0   | 3740 | 2.9233          | 0.0    | 0.0    | 0.0    | 0.0       |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
