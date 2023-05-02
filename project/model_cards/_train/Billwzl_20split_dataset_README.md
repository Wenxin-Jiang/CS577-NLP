---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: 20split_dataset
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 20split_dataset

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0446

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
- train_batch_size: 64
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 2.5971        | 1.0   | 11851 | 2.3479          |
| 2.3773        | 2.0   | 23702 | 2.2446          |
| 2.2663        | 3.0   | 35553 | 2.1630          |
| 2.1842        | 4.0   | 47404 | 2.1059          |
| 2.1145        | 5.0   | 59255 | 2.0626          |
| 2.0652        | 6.0   | 71106 | 2.0446          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1