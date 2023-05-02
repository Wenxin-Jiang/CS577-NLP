---
license: mit
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bart-large-cnn-samsum-ElectrifAi_v7
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-large-cnn-samsum-ElectrifAi_v7

This model is a fine-tuned version of [philschmid/bart-large-cnn-samsum](https://huggingface.co/philschmid/bart-large-cnn-samsum) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3396
- Rouge1: 53.6259
- Rouge2: 29.3085
- Rougel: 39.5423
- Rougelsum: 51.4836
- Gen Len: 105.963

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
| No log        | 1.0   | 24   | 1.3377          | 53.4184 | 29.2938 | 38.7671 | 51.2253   | 114.9259 |
| No log        | 2.0   | 48   | 1.3225          | 53.1653 | 29.2807 | 40.6062 | 50.9565   | 116.037  |
| No log        | 3.0   | 72   | 1.3396          | 53.6259 | 29.3085 | 39.5423 | 51.4836   | 105.963  |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1
- Datasets 2.6.1
- Tokenizers 0.13.2
