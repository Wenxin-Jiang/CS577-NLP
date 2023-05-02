---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: twitter-climate-sentiment-model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter-climate-sentiment-model

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.2779
- eval_accuracy: 0.8941
- eval_f1: 0.9372
- eval_runtime: 135.2041
- eval_samples_per_second: 39.873
- eval_steps_per_second: 2.493
- epoch: 1.0
- step: 1348

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
- Datasets 2.5.2
- Tokenizers 0.12.1
