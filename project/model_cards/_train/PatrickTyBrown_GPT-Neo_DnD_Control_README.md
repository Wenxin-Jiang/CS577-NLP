---
tags:
- generated_from_trainer
model-index:
- name: GPT-Neo_DnD_Control
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# GPT-Neo_DnD_Control

This model is a fine-tuned version of [PatrickTyBrown/GPT-Neo_DnD](https://huggingface.co/PatrickTyBrown/GPT-Neo_DnD) on the None dataset.
It achieves the following results on the evaluation set:
- eval_loss: 2.6518
- eval_runtime: 141.422
- eval_samples_per_second: 6.527
- eval_steps_per_second: 3.267
- epoch: 3.9
- step: 36000

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1.5e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
