---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: sentiment-model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sentiment-model

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.4302
- eval_accuracy: 0.8337
- eval_f1: 0.0
- eval_runtime: 25.9665
- eval_samples_per_second: 30.809
- eval_steps_per_second: 1.926
- epoch: 1.0
- step: 200

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
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cpu
- Tokenizers 0.12.1
