---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- vivos_dataset
model-index:
- name: test285
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# test285

This model is a fine-tuned version of [aiface/cv8](https://huggingface.co/aiface/cv8) on the vivos_dataset dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.3865
- eval_wer: 0.3012
- eval_runtime: 39.5722
- eval_samples_per_second: 19.205
- eval_steps_per_second: 2.401
- epoch: 1.1
- step: 400

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.19.2
- Pytorch 1.10.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
