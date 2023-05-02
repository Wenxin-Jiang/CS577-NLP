---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: distilbert-base-uncased-ner-invoiceSenderName_all_inv_20_12
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-ner-invoiceSenderName_all_inv_20_12

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.0145
- eval_precision: 0.0
- eval_recall: 0.0
- eval_f1: 0.0
- eval_accuracy: 0.9957
- eval_runtime: 511.2392
- eval_samples_per_second: 42.113
- eval_steps_per_second: 2.633
- epoch: 4.0
- step: 30500

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
- num_epochs: 20

### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0
- Datasets 2.3.2
- Tokenizers 0.10.3
