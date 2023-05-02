---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- spearmanr
model-index:
- name: M1_cross
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# M1_cross

This model is a fine-tuned version of [albert-base-v2](https://huggingface.co/albert-base-v2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0066
- Pearson: 0.9828
- Spearmanr: 0.9147

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
- seed: 25
- optimizer: Adam with betas=(0.9,0.98) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 125.0
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Pearson | Spearmanr |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:---------:|
| 0.0294        | 1.0   | 131  | 0.0457          | 0.8770  | 0.8351    |
| 0.0237        | 2.0   | 262  | 0.0302          | 0.9335  | 0.8939    |
| 0.015         | 3.0   | 393  | 0.0155          | 0.9594  | 0.9054    |
| 0.0177        | 4.0   | 524  | 0.0106          | 0.9778  | 0.9091    |
| 0.0087        | 5.0   | 655  | 0.0066          | 0.9828  | 0.9147    |


### Framework versions

- Transformers 4.20.0
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
