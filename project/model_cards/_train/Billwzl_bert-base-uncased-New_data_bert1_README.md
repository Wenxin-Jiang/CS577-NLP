---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: bert-base-uncased-New_data_bert1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-New_data_bert1

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9215

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 16

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 2.4496        | 1.0   | 2018  | 2.2066          |
| 2.2532        | 2.0   | 4036  | 2.1438          |
| 2.1572        | 3.0   | 6054  | 2.1046          |
| 2.0839        | 4.0   | 8072  | 2.0943          |
| 2.0222        | 5.0   | 10090 | 2.0573          |
| 1.9608        | 6.0   | 12108 | 2.0188          |
| 1.9123        | 7.0   | 14126 | 2.0008          |
| 1.8666        | 8.0   | 16144 | 2.0063          |
| 1.8305        | 9.0   | 18162 | 1.9607          |
| 1.7958        | 10.0  | 20180 | 1.9702          |
| 1.7498        | 11.0  | 22198 | 1.9635          |
| 1.7172        | 12.0  | 24216 | 1.9404          |
| 1.695         | 13.0  | 26234 | 1.9455          |
| 1.6628        | 14.0  | 28252 | 1.9269          |
| 1.6558        | 15.0  | 30270 | 1.9173          |
| 1.6293        | 16.0  | 32288 | 1.9215          |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
