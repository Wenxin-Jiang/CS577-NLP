---
license: mit
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bart-large-cnn-samsum-ElectrifAi_v3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-large-cnn-samsum-ElectrifAi_v3

This model is a fine-tuned version of [philschmid/bart-large-cnn-samsum](https://huggingface.co/philschmid/bart-large-cnn-samsum) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8053
- Rouge1: 62.0348
- Rouge2: 41.9592
- Rougel: 49.1046
- Rougelsum: 59.4965
- Gen Len: 101.2747

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len  |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:--------:|
| No log        | 1.0   | 23   | 1.1760          | 54.8264 | 32.0931 | 40.5826 | 52.2503   | 99.4505  |
| No log        | 2.0   | 46   | 0.9005          | 59.7325 | 38.3487 | 45.8861 | 56.9922   | 108.3846 |
| No log        | 3.0   | 69   | 0.8053          | 62.0348 | 41.9592 | 49.1046 | 59.4965   | 101.2747 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1
- Datasets 2.6.1
- Tokenizers 0.13.2
