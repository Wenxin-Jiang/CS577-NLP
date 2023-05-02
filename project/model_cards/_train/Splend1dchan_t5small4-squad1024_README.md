---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: t5small4-squad1024
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5small4-squad1024

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- distributed_type: tpu
- gradient_accumulation_steps: 16
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results



### Framework versions

- Transformers 4.18.0.dev0
- Pytorch 1.9.0+cu102
- Tokenizers 0.11.6
