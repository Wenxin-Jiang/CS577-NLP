---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- XpCo
model-index:
- name: XpCoDir2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# XpCoDir2

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the XpCoDataset dataset.

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Framework versions

- Transformers 4.16.2
- Pytorch 1.9.0
- Datasets 2.0.0
- Tokenizers 0.10.3
