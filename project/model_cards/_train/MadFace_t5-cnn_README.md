---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-cnn
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-cnn

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4562
- Rouge1: 25.1836
- Rouge2: 12.0806
- Rougel: 20.818
- Rougelsum: 23.6868
- Gen Len: 18.9986

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2  | Rougel | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:------:|:---------:|:-------:|
| 1.4286        | 1.0   | 50000 | 1.4562          | 25.1836 | 12.0806 | 20.818 | 23.6868   | 18.9986 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
