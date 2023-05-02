---
tags:
- generated_from_trainer
datasets:
- imdb
model-index:
- name: phobert-base-finetuned-imdb
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# phobert-base-finetuned-imdb

This model is a fine-tuned version of [vinai/phobert-base](https://huggingface.co/vinai/phobert-base) on the imdb dataset.
It achieves the following results on the evaluation set:
- Loss: 2.6149

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 3.3266        | 1.0   | 157  | 2.7949          |
| 2.9162        | 2.0   | 314  | 2.6515          |
| 2.8177        | 3.0   | 471  | 2.6452          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
