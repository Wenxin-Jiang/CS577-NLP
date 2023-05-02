---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- lst20
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: premodel
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: lst20
      type: lst20
      config: default
      split: train
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.8533733110439704
    - name: Recall
      type: recall
      value: 0.8653846153846154
    - name: F1
      type: f1
      value: 0.8593369935367294
    - name: Accuracy
      type: accuracy
      value: 0.9477067610537897
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# premodel

This model is a fine-tuned version of [Geotrend/bert-base-th-cased](https://huggingface.co/Geotrend/bert-base-th-cased) on the lst20 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1761
- Precision: 0.8534
- Recall: 0.8654
- F1: 0.8593
- Accuracy: 0.9477

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results



### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.0
- Tokenizers 0.13.2
