---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-small-devices-sum-ver2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-devices-sum-ver2

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3679
- Rouge1: 90.6465
- Rouge2: 65.2833
- Rougel: 90.6707
- Rougelsum: 90.7313
- Gen Len: 4.4702

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
| No log        | 1.0   | 91   | 1.0957          | 58.9566 | 33.4113 | 58.8004 | 58.8863   | 4.8308  |
| No log        | 2.0   | 182  | 0.7017          | 78.9566 | 49.9716 | 78.9338 | 78.9643   | 4.3329  |
| No log        | 3.0   | 273  | 0.5386          | 84.8786 | 56.9622 | 84.8204 | 84.9117   | 4.4577  |
| No log        | 4.0   | 364  | 0.4693          | 87.9792 | 61.0779 | 87.8795 | 88.0098   | 4.4383  |
| No log        | 5.0   | 455  | 0.4273          | 89.4667 | 63.1994 | 89.4169 | 89.5197   | 4.4743  |
| 1.0586        | 6.0   | 546  | 0.4002          | 89.6456 | 63.5041 | 89.6062 | 89.7042   | 4.4452  |
| 1.0586        | 7.0   | 637  | 0.3848          | 89.9993 | 64.2505 | 89.9775 | 90.0651   | 4.423   |
| 1.0586        | 8.0   | 728  | 0.3752          | 90.4249 | 64.819  | 90.4434 | 90.5111   | 4.4799  |
| 1.0586        | 9.0   | 819  | 0.3703          | 90.4689 | 65.0086 | 90.4954 | 90.5632   | 4.4632  |
| 1.0586        | 10.0  | 910  | 0.3679          | 90.6465 | 65.2833 | 90.6707 | 90.7313   | 4.4702  |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
