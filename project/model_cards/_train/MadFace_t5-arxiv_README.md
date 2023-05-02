---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-arxiv
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-arxiv

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3852
- Rouge1: 18.0722
- Rouge2: 6.8453
- Rougel: 14.3659
- Rougelsum: 16.4137
- Gen Len: 19.0

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| 2.5169        | 1.0   | 12500 | 2.3852          | 18.0722 | 6.8453 | 14.3659 | 16.4137   | 19.0    |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
