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
- Loss: 3.0294
- Rouge1: 16.6807
- Rouge2: 8.0004
- Rougel: 16.2251
- Rougelsum: 16.1743

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
| 6.5928        | 1.0   | 1209 | 3.3005          | 14.7863 | 6.5038 | 14.3031 | 14.2522   |
| 3.9024        | 2.0   | 2418 | 3.1399          | 16.9257 | 8.6583 | 16.15   | 16.1299   |
| 3.5806        | 3.0   | 3627 | 3.0869          | 18.2734 | 9.1667 | 17.7441 | 17.5782   |
| 3.4201        | 4.0   | 4836 | 3.0590          | 17.763  | 8.9447 | 17.1833 | 17.1661   |
| 3.3202        | 5.0   | 6045 | 3.0598          | 17.7754 | 8.5695 | 17.4139 | 17.2653   |
| 3.2436        | 6.0   | 7254 | 3.0409          | 16.8423 | 8.1593 | 16.5392 | 16.4297   |
| 3.2079        | 7.0   | 8463 | 3.0332          | 16.8991 | 8.1574 | 16.4229 | 16.3515   |
| 3.1801        | 8.0   | 9672 | 3.0294          | 16.6807 | 8.0004 | 16.2251 | 16.1743   |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1
