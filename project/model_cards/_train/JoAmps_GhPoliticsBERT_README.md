---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: GhPoliticsBERT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# GhPoliticsBERT

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0000

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.0           | 1.0   | 9188  | 0.0000          |
| 0.0           | 2.0   | 18376 | 0.0000          |
| 0.0           | 3.0   | 27564 | 0.0000          |
| 0.0           | 4.0   | 36752 | 0.0000          |
| 0.0           | 5.0   | 45940 | 0.0000          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1
- Datasets 2.6.1
- Tokenizers 0.13.1
