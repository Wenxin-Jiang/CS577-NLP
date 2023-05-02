---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
model-index:
- name: BERT_Mod_2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERT_Mod_2

This model is a fine-tuned version of [distilbert-base-cased](https://huggingface.co/distilbert-base-cased) on the glue dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.5659
- eval_accuracy: 0.9037
- eval_runtime: 0.3838
- eval_samples_per_second: 2271.724
- eval_steps_per_second: 143.285
- epoch: 0.01
- step: 49

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
- num_epochs: 5

### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0
- Datasets 2.4.0
- Tokenizers 0.12.1
