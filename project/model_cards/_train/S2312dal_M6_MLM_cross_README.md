---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- spearmanr
model-index:
- name: M6_MLM_cross
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# M6_MLM_cross

This model is a fine-tuned version of [S2312dal/M6_MLM](https://huggingface.co/S2312dal/M6_MLM) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0197
- Pearson: 0.9680
- Spearmanr: 0.9098

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 8.0
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Pearson | Spearmanr |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:---------:|
| 0.0723        | 1.0   | 131  | 0.0646          | 0.8674  | 0.8449    |
| 0.0433        | 2.0   | 262  | 0.0322          | 0.9475  | 0.9020    |
| 0.0015        | 3.0   | 393  | 0.0197          | 0.9680  | 0.9098    |


### Framework versions

- Transformers 4.20.0
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
