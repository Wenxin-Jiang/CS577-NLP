---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: whisper-base-en
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-base-en

This model is a fine-tuned version of [openai/whisper-base](https://huggingface.co/openai/whisper-base) on the None dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 1000
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
