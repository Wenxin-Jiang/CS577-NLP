---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-small-finetuned-amazon-en-es
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-small-finetuned-amazon-en-es

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.0346
- Rouge1: 16.8527
- Rouge2: 8.331
- Rougel: 16.4475
- Rougelsum: 16.6421

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|
| 6.7536        | 1.0   | 1209 | 3.2881          | 13.6319 | 5.4635 | 13.0552 | 13.1093   |
| 3.9312        | 2.0   | 2418 | 3.1490          | 16.8402 | 8.3559 | 16.1876 | 16.2869   |
| 3.5987        | 3.0   | 3627 | 3.1043          | 17.9887 | 9.3136 | 17.3034 | 17.4313   |
| 3.4261        | 4.0   | 4836 | 3.0573          | 17.0089 | 8.7389 | 16.5351 | 16.5023   |
| 3.3221        | 5.0   | 6045 | 3.0569          | 16.8461 | 8.0988 | 16.4898 | 16.4927   |
| 3.2549        | 6.0   | 7254 | 3.0511          | 17.3428 | 8.2234 | 16.7312 | 16.8749   |
| 3.2067        | 7.0   | 8463 | 3.0334          | 16.268  | 7.9729 | 15.9342 | 16.0065   |
| 3.1842        | 8.0   | 9672 | 3.0346          | 16.8527 | 8.331  | 16.4475 | 16.6421   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
