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
- name: wikigold_trained_no_DA_testing2
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
      value: 0.8410852713178295
    - name: Recall
      type: recall
      value: 0.84765625
    - name: F1
      type: f1
      value: 0.8443579766536965
    - name: Accuracy
      type: accuracy
      value: 0.9571820972693489
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wikigold_trained_no_DA_testing2

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the wikigold_splits dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1431
- Precision: 0.8411
- Recall: 0.8477
- F1: 0.8444
- Accuracy: 0.9572

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
| No log        | 1.0   | 167  | 0.1618          | 0.7559    | 0.75   | 0.7529 | 0.9410   |
| No log        | 2.0   | 334  | 0.1488          | 0.8384    | 0.8242 | 0.8313 | 0.9530   |
| 0.1589        | 3.0   | 501  | 0.1431          | 0.8411    | 0.8477 | 0.8444 | 0.9572   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
