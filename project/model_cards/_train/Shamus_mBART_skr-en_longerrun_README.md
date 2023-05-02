---
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: mBART_skr-en_longerrun
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mBART_skr-en_longerrun

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4577
- Bleu: 30.8071
- Gen Len: 34.548

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
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|
| 0.5444        | 0.72  | 500  | 1.3416          | 28.7505 | 34.228  |
| 0.8576        | 1.45  | 1000 | 1.3411          | 30.1776 | 34.328  |
| 0.6422        | 2.18  | 1500 | 1.3882          | 30.2815 | 34.164  |
| 0.532         | 2.9   | 2000 | 1.3716          | 30.8947 | 34.556  |
| 0.4473        | 3.63  | 2500 | 1.4577          | 30.8071 | 34.548  |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
