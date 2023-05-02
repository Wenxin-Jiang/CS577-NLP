---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- spearmanr
model-index:
- name: M6_cross
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# M6_cross

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0084
- Pearson: 0.9811
- Spearmanr: 0.9075

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
- train_batch_size: 20
- eval_batch_size: 20
- seed: 25
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 6.0
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Pearson | Spearmanr |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:---------:|
| 0.0059        | 1.0   | 105  | 0.0158          | 0.9633  | 0.9054    |
| 0.001         | 2.0   | 210  | 0.0102          | 0.9770  | 0.9103    |
| 0.0008        | 3.0   | 315  | 0.0083          | 0.9805  | 0.9052    |
| 0.0011        | 4.0   | 420  | 0.0075          | 0.9812  | 0.9082    |
| 0.0017        | 5.0   | 525  | 0.0084          | 0.9811  | 0.9075    |


### Framework versions

- Transformers 4.20.0
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
