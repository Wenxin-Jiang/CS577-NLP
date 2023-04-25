---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-base-wikinewssum-italian
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-base-wikinewssum-italian

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 10.5739
- Rouge1: 2.1728
- Rouge2: 0.1516
- Rougel: 2.0846
- Rougelsum: 2.0515

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
| No log        | 1.0   | 8    | 16.6193         | 2.4011 | 0.3829 | 2.1505 | 2.2161    |
| No log        | 2.0   | 16   | 15.8909         | 2.5165 | 0.2799 | 2.3403 | 2.3523    |
| No log        | 3.0   | 24   | 15.4843         | 2.2794 | 0.2252 | 2.1849 | 2.1382    |
| 17.2559       | 4.0   | 32   | 13.0850         | 2.2448 | 0.1516 | 2.1426 | 2.0859    |
| 17.2559       | 5.0   | 40   | 11.7838         | 2.2448 | 0.1516 | 2.1426 | 2.0859    |
| 17.2559       | 6.0   | 48   | 11.3207         | 2.2424 | 0.1516 | 2.1423 | 2.1171    |
| 17.2559       | 7.0   | 56   | 10.7871         | 2.1081 | 0.1516 | 2.0227 | 1.9838    |
| 14.6026       | 8.0   | 64   | 10.5739         | 2.1728 | 0.1516 | 2.0846 | 2.0515    |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.1
- Datasets 1.16.1
- Tokenizers 0.10.3
