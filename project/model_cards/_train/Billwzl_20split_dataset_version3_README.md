---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: 20split_dataset_version3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 20split_dataset_version3

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.8310

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 16

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 3.1679        | 1.0   | 313  | 2.9768          |
| 2.9869        | 2.0   | 626  | 2.9299          |
| 2.8528        | 3.0   | 939  | 2.9176          |
| 2.7435        | 4.0   | 1252 | 2.9104          |
| 2.6458        | 5.0   | 1565 | 2.8863          |
| 2.5865        | 6.0   | 1878 | 2.8669          |
| 2.5218        | 7.0   | 2191 | 2.8802          |
| 2.4647        | 8.0   | 2504 | 2.8639          |
| 2.3933        | 9.0   | 2817 | 2.8543          |
| 2.3687        | 10.0  | 3130 | 2.8573          |
| 2.3221        | 11.0  | 3443 | 2.8398          |
| 2.276         | 12.0  | 3756 | 2.8415          |
| 2.2379        | 13.0  | 4069 | 2.8471          |
| 2.2427        | 14.0  | 4382 | 2.8318          |
| 2.1741        | 15.0  | 4695 | 2.8356          |
| 2.1652        | 16.0  | 5008 | 2.8310          |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
