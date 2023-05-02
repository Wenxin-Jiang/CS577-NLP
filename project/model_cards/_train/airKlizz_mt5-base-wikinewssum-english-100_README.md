---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-base-wikinewssum-english-100
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-base-wikinewssum-english-100

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 6.6225
- Rouge1: 3.909
- Rouge2: 0.9312
- Rougel: 3.3835
- Rougelsum: 3.7786

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| No log        | 0.96  | 12   | 14.4949         | 2.7398 | 0.7181 | 2.491  | 2.6561    |
| No log        | 1.96  | 24   | 10.5056         | 4.4428 | 1.4293 | 3.8469 | 4.2869    |
| No log        | 2.96  | 36   | 8.9856          | 4.1179 | 1.229  | 3.5726 | 3.9693    |
| No log        | 3.96  | 48   | 7.7950          | 3.9217 | 1.1339 | 3.4256 | 3.7905    |
| No log        | 4.96  | 60   | 7.0734          | 3.8004 | 1.0326 | 3.3246 | 3.6766    |
| No log        | 5.96  | 72   | 6.7897          | 3.6351 | 0.9162 | 3.1839 | 3.5149    |
| No log        | 6.96  | 84   | 6.6610          | 3.7486 | 0.8829 | 3.2583 | 3.6193    |
| No log        | 7.96  | 96   | 6.6225          | 3.909  | 0.9312 | 3.3835 | 3.7786    |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.1
- Datasets 1.16.1
- Tokenizers 0.10.3
