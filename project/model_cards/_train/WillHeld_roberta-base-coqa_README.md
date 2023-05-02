---
license: mit
tags:
- generated_from_trainer
datasets:
- coqa
model-index:
- name: roberta-base-coqa
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-coqa

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the coqa dataset.

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 10.0

### Training results



### Framework versions

- Transformers 4.21.3
- Pytorch 1.7.1
- Datasets 1.18.3
- Tokenizers 0.11.6
