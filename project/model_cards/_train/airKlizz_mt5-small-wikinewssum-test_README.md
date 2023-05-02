---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-small-wikinewssum-test
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-small-wikinewssum-test

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.9354
- Rouge1: 6.8433
- Rouge2: 2.5498
- Rougel: 5.6114
- Rougelsum: 6.353

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
- train_batch_size: 12
- eval_batch_size: 12
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| No log        | 1.0   | 661  | 3.2810          | 6.4161 | 2.403  | 5.3674 | 6.0329    |
| No log        | 2.0   | 1322 | 3.1515          | 6.9291 | 2.6826 | 5.6839 | 6.4359    |
| No log        | 3.0   | 1983 | 3.0565          | 6.7939 | 2.6113 | 5.6133 | 6.3126    |
| No log        | 4.0   | 2644 | 2.9815          | 6.0279 | 2.1637 | 4.9892 | 5.5962    |
| No log        | 5.0   | 3305 | 2.9645          | 6.3926 | 2.339  | 5.2716 | 5.9443    |
| 3.9937        | 6.0   | 3966 | 2.9476          | 6.4739 | 2.3615 | 5.3473 | 6.0089    |
| 3.9937        | 7.0   | 4627 | 2.9405          | 6.615  | 2.4309 | 5.4493 | 6.1445    |
| 3.9937        | 8.0   | 5288 | 2.9354          | 6.8433 | 2.5498 | 5.6114 | 6.353     |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.1
- Datasets 1.16.1
- Tokenizers 0.10.3
