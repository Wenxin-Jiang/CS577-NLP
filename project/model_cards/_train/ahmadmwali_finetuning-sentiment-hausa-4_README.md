---
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: finetuning-sentiment-hausa-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuning-sentiment-hausa-4

This model is a fine-tuned version of [castorini/afriberta_large](https://huggingface.co/castorini/afriberta_large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3976
- Accuracy: 0.8848
- F1: 0.8850

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results



### Framework versions

- Transformers 4.24.0
- Pytorch 1.8.2+cu111
- Datasets 2.6.1
- Tokenizers 0.13.2
