---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-small-ipad-sum
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-ipad-sum

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3632
- Rouge1: 90.6
- Rouge2: 29.6667
- Rougel: 90.8667
- Rougelsum: 90.6667
- Gen Len: 4.79

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
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 13   | 2.7713          | 20.7123 | 0.7601  | 20.6467 | 20.6954   | 18.85   |
| No log        | 2.0   | 26   | 1.9722          | 23.2307 | 1.3571  | 23.263  | 23.2952   | 18.25   |
| No log        | 3.0   | 39   | 1.2886          | 46.3724 | 8.0862  | 46.5163 | 46.4406   | 13.7    |
| No log        | 4.0   | 52   | 0.8267          | 78.4825 | 14.1975 | 78.6464 | 78.3548   | 7.38    |
| No log        | 5.0   | 65   | 0.6405          | 81.8222 | 15.7532 | 81.8856 | 81.88     | 6.3     |
| No log        | 6.0   | 78   | 0.5210          | 83.2111 | 17.5    | 83.2931 | 83.1583   | 5.46    |
| No log        | 7.0   | 91   | 0.4425          | 87.154  | 21.7917 | 87.2008 | 87.169    | 4.99    |
| No log        | 8.0   | 104  | 0.3974          | 89.7619 | 27.6667 | 89.8571 | 89.8817   | 4.85    |
| No log        | 9.0   | 117  | 0.3735          | 90.4    | 29.6667 | 90.5706 | 90.4635   | 4.87    |
| No log        | 10.0  | 130  | 0.3632          | 90.6    | 29.6667 | 90.8667 | 90.6667   | 4.79    |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
