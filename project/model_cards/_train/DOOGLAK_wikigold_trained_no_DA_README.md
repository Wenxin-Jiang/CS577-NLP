---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wikigold_splits
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: temp
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wikigold_splits
      type: wikigold_splits
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.8517110266159695
    - name: Recall
      type: recall
      value: 0.875
    - name: F1
      type: f1
      value: 0.8631984585741811
    - name: Accuracy
      type: accuracy
      value: 0.9607367910809501
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# temp

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the wikigold_splits dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1322
- Precision: 0.8517
- Recall: 0.875
- F1: 0.8632
- Accuracy: 0.9607

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

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 167  | 0.1490          | 0.7583    | 0.7760 | 0.7671 | 0.9472   |
| No log        | 2.0   | 334  | 0.1337          | 0.8519    | 0.8464 | 0.8491 | 0.9572   |
| 0.1569        | 3.0   | 501  | 0.1322          | 0.8517    | 0.875  | 0.8632 | 0.9607   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
