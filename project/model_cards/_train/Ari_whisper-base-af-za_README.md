---
language:
- af
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- google/fleurs
model-index:
- name: whisper-base-af-za-V4-Ari
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-base-af-za-V4-Ari

This model is a fine-tuned version of [openai/whisper-base](https://huggingface.co/openai/whisper-base) on the Google FLEURS dataset.
It achieves the following results on the evaluation set:
- eval_loss: 1.0084
- eval_wer: 32.0267
- eval_runtime: 152.7461
- eval_samples_per_second: 6.154
- eval_steps_per_second: 0.386
- epoch: 51.14
- step: 4500

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
- train_batch_size: 64
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu116
- Datasets 2.8.1.dev0
- Tokenizers 0.13.2
