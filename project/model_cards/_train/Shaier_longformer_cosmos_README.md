---
tags:
- generated_from_trainer
datasets:
- cosmos_qa
model-index:
- name: longformer_cosmos
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# longformer_cosmos

This model was trained from scratch on the cosmos_qa dataset.

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 25
- total_train_batch_size: 100
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1
- Datasets 2.5.1
- Tokenizers 0.11.0
