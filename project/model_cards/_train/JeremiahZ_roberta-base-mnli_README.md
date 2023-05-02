---
language:
- en
tags:
- generated_from_trainer
datasets:
- glue
model-index:
- name: roberta-base-mnli
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-mnli

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base/) on the GLUE MNLI dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.7539
- eval_accuracy: 0.8697
- eval_runtime: 25.5655
- eval_samples_per_second: 384.581
- eval_steps_per_second: 48.073
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
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 10.0

### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
