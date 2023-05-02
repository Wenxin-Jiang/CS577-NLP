---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-small-devices-sum-ver3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-devices-sum-ver3

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1325
- Rouge1: 95.6631
- Rouge2: 83.6149
- Rougel: 95.6622
- Rougelsum: 95.6632
- Gen Len: 4.9279

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
| No log        | 1.0   | 467  | 0.3307          | 90.9817 | 74.3762 | 90.9596 | 90.9781   | 4.7527  |
| 1.0254        | 2.0   | 934  | 0.2365          | 92.6761 | 78.1252 | 92.6664 | 92.6682   | 4.8004  |
| 0.3526        | 3.0   | 1401 | 0.1904          | 93.8503 | 80.4523 | 93.8286 | 93.8338   | 4.8221  |
| 0.2643        | 4.0   | 1868 | 0.1638          | 94.8079 | 82.1779 | 94.7815 | 94.7853   | 4.917   |
| 0.2075        | 5.0   | 2335 | 0.1503          | 95.1619 | 82.6284 | 95.1533 | 95.1578   | 4.9263  |
| 0.1831        | 6.0   | 2802 | 0.1408          | 95.2357 | 82.8152 | 95.2261 | 95.2263   | 4.9287  |
| 0.161         | 7.0   | 3269 | 0.1386          | 95.4993 | 83.2609 | 95.4935 | 95.4933   | 4.9269  |
| 0.1589        | 8.0   | 3736 | 0.1344          | 95.6363 | 83.4727 | 95.6304 | 95.632    | 4.9309  |
| 0.1517        | 9.0   | 4203 | 0.1330          | 95.6702 | 83.6329 | 95.6669 | 95.6736   | 4.9301  |
| 0.1436        | 10.0  | 4670 | 0.1325          | 95.6631 | 83.6149 | 95.6622 | 95.6632   | 4.9279  |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
