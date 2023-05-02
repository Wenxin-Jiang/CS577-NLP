---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: finetune_sentiment_improved_v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetune_sentiment_improved_v1

This model is a fine-tuned version of [cross-encoder/ms-marco-electra-base](https://huggingface.co/cross-encoder/ms-marco-electra-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9743
- Accuracy: 0.6696
- F1: 0.6696
- Precision: 0.6696
- Recall: 0.6696

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
- num_epochs: 10

### Training results



### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.2
