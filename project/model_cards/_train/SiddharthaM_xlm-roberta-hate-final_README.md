---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: xlm-roberta-hate-final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-hate-final

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4961
- Accuracy: 0.8061
- Precision: 0.8145
- Recall: 0.8061
- F1: 0.7997

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 1.0   | 296  | 0.4747          | 0.7652   | 0.8023    | 0.7652 | 0.7456 |
| 0.5446        | 2.0   | 592  | 0.4620          | 0.7918   | 0.8183    | 0.7918 | 0.7789 |
| 0.5446        | 3.0   | 888  | 0.4580          | 0.8042   | 0.8144    | 0.8042 | 0.7971 |
| 0.453         | 4.0   | 1184 | 0.4534          | 0.7985   | 0.8071    | 0.7985 | 0.7915 |
| 0.453         | 5.0   | 1480 | 0.4749          | 0.8051   | 0.8147    | 0.8051 | 0.7983 |
| 0.406         | 6.0   | 1776 | 0.4961          | 0.8061   | 0.8145    | 0.8061 | 0.7997 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
