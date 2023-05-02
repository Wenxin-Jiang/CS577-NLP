---
tags:
- generated_from_trainer
model-index:
- name: lin_xlmr
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# lin_xlmr

This model is a fine-tuned version of [models/lin_xlmr/](https://huggingface.co/models/lin_xlmr/) on an unknown dataset.
It achieves the following results on the evaluation set:
- eval_loss: 2.1469
- eval_runtime: 22.8128
- eval_samples_per_second: 32.175
- eval_steps_per_second: 4.033
- step: 0

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
- train_batch_size: 5
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- gradient_accumulation_steps: 2
- total_train_batch_size: 10
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Framework versions

- Transformers 4.21.1
- Pytorch 1.7.1+cu110
- Datasets 1.16.1
- Tokenizers 0.12.1
