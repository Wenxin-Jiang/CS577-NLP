---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: checkpoint-24453
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# checkpoint-24453

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.

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
- train_batch_size: 12
- eval_batch_size: 12
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 48
- optimizer: Adafactor
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 6000
- num_epochs: 30

### Framework versions

- Transformers 4.18.0
- Pytorch 1.5.0
- Datasets 2.4.0
- Tokenizers 0.12.1
