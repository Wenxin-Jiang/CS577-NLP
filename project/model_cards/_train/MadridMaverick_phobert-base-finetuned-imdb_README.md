---
tags:
- generated_from_trainer
model-index:
- name: phobert-base-finetuned-imdb
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# phobert-base-finetuned-imdb

This model is a fine-tuned version of [vinai/phobert-base](https://huggingface.co/vinai/phobert-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2510

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.7146        | 1.0   | 2500 | 1.4245          |
| 1.3821        | 2.0   | 5000 | 1.2666          |
| 1.3308        | 3.0   | 7500 | 1.2564          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
