---
tags:
- generated_from_trainer
datasets:
- xsum
model-index:
- name: flan-t5-large-summarization-finetuned-xsum
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# flan-t5-large-summarization-finetuned-xsum

This model was trained from scratch on the xsum dataset.

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
- train_batch_size: 3
- eval_batch_size: 3
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1
- Datasets 2.6.1
- Tokenizers 0.13.2
