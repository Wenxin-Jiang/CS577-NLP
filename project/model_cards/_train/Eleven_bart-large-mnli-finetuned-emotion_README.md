---
license: mit
tags:
- generated_from_trainer
model-index:
- name: bart-large-mnli-finetuned-emotion
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-large-mnli-finetuned-emotion

This model is a fine-tuned version of [facebook/bart-large-mnli](https://huggingface.co/facebook/bart-large-mnli) on an unknown dataset.

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
- train_batch_size: 6
- eval_batch_size: 6
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Tokenizers 0.12.1
