---
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: finetuned_cont
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_cont

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4785
- Accuracy: 0.7715
- F1: 0.7703

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-06
- train_batch_size: 16
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.4967        | 1.0   | 625  | 0.4989          | 0.7565   | 0.7542 |
| 0.4727        | 2.0   | 1250 | 0.4830          | 0.773    | 0.7669 |
| 0.4559        | 3.0   | 1875 | 0.4887          | 0.772    | 0.7637 |
| 0.4395        | 4.0   | 2500 | 0.4785          | 0.7715   | 0.7703 |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.12.1+cu113
- Datasets 1.16.1
- Tokenizers 0.10.3
