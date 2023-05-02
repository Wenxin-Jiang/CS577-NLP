---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: dgpt
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dgpt

This model is a fine-tuned version of [distilgpt2](https://huggingface.co/distilgpt2) on an unknown dataset.

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
- eval_batch_size: 8
- seed: 42
- distributed_type: tpu
- num_devices: 8
- total_train_batch_size: 16
- total_eval_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10.0

### Training results



### Framework versions

- Transformers 4.14.0.dev0
- Pytorch 1.9.0+cu102
- Datasets 1.16.2.dev0
- Tokenizers 0.10.3
hello
hello
