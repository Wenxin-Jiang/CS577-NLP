---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: bert-base-multilingual-uncased-sep-26
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-multilingual-uncased-sep-26

This model is a fine-tuned version of [bert-base-multilingual-uncased](https://huggingface.co/bert-base-multilingual-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0483
- F1: 0.9369

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 0.0798        | 1.0   | 8623  | 0.0682          | 0.8979 |
| 0.0498        | 2.0   | 17246 | 0.0551          | 0.9270 |
| 0.0351        | 3.0   | 25869 | 0.0483          | 0.9369 |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1
