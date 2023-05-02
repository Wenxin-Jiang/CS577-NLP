---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- conll2003
model-index:
- name: bert-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.0593
- eval_precision: 0.9293
- eval_recall: 0.9485
- eval_f1: 0.9388
- eval_accuracy: 0.9858
- eval_runtime: 120.5431
- eval_samples_per_second: 26.97
- eval_steps_per_second: 3.376
- epoch: 2.0
- step: 3512

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
- num_epochs: 3

### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cpu
- Datasets 2.2.2
- Tokenizers 0.12.1
