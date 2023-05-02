---
tags:
- generated_from_trainer
model-index:
- name: weights
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# weights

This model was trained from pretrained(GPT2-medium) weights on Harry Potter dataset:
https://www.kaggle.com/datasets/moxxis/harry-potter-lstm

## Model description

GPT2-medium

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 10
- num_epochs: 217

### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cpu
- Datasets 2.1.0
- Tokenizers 0.12.1
