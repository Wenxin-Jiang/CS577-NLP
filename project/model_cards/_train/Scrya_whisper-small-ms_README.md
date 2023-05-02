---
language:
- ms
license: apache-2.0
tags:
- whisper-event
- incomplete
- generated_from_trainer
datasets:
- google/fleurs
model-index:
- name: Whisper Small MS - FLEURS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small MS - FLEURS

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the FLEURS dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.3324
- eval_wer: 15.6453
- eval_runtime: 347.6066
- eval_samples_per_second: 2.155
- eval_steps_per_second: 0.27
- epoch: 10.75
- step: 1000

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
