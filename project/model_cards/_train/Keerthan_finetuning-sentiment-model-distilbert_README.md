---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: finetuning-sentiment-model-distilbert
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuning-sentiment-model-distilbert

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.5942
- eval_accuracy: 0.9189
- eval_f1: 0.9154
- eval_runtime: 114.314
- eval_samples_per_second: 69.983
- eval_steps_per_second: 8.748
- epoch: 9.0
- step: 36000

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
