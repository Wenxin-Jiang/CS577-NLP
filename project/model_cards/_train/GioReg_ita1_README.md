---
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: ita1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ita1

This model is a fine-tuned version of [m-polignano-uniba/bert_uncased_L-12_H-768_A-12_italian_alb3rt0](https://huggingface.co/m-polignano-uniba/bert_uncased_L-12_H-768_A-12_italian_alb3rt0) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5892
- Accuracy: 0.776
- F1: 0.5912

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

### Training results



### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
