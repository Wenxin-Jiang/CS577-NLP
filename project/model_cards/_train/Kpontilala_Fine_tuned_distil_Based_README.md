---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: Fine_tuned_distil_Based
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Fine_tuned_distil_Based

This model is a fine-tuned version of [distilbert-base-cased](https://huggingface.co/distilbert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.7217
- eval_accuracy: 0.7317
- eval_runtime: 48.8174
- eval_samples_per_second: 61.454
- eval_steps_per_second: 7.682
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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
