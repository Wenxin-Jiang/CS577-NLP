---
tags:
- generated_from_trainer
datasets:
- cnn_dailymail
model-index:
- name: Wayne_NLP_mT5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Wayne_NLP_mT5

This model was trained only english datasets.
if you want trained korean + english model
go to wayne_mulang_mT5.

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 10

### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0a0+3fd9dcf
- Datasets 1.18.3
- Tokenizers 0.11.0
