---
license: mit
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bart-large-cnn-samsum-ElectrifAi_v9
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-large-cnn-samsum-ElectrifAi_v9

This model is a fine-tuned version of [philschmid/bart-large-cnn-samsum](https://huggingface.co/philschmid/bart-large-cnn-samsum) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2325
- Rouge1: 55.1928
- Rouge2: 33.3871
- Rougel: 43.865
- Rougelsum: 54.1984
- Gen Len: 108.8667

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
| No log        | 1.0   | 27   | 1.2252          | 55.969  | 34.0884 | 43.1389 | 54.7972   | 108.0    |
| No log        | 2.0   | 54   | 1.2156          | 55.834  | 34.3509 | 43.5382 | 54.4829   | 102.8    |
| No log        | 3.0   | 81   | 1.2325          | 55.1928 | 33.3871 | 43.865  | 54.1984   | 108.8667 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1
- Datasets 2.6.1
- Tokenizers 0.13.2
