---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- itihasa
model-index:
- name: t5-base-finetuned-sn-to-en
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-finetuned-sn-to-en

This model is a fine-tuned version of [google/t5-v1_1-base](https://huggingface.co/google/t5-v1_1-base) on the itihasa dataset.

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
- num_epochs: 1
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.17.0
- Tokenizers 0.10.3
