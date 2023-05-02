---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article100v7_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_100v7_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article100v7_wikigold_split
      type: article100v7_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.4197698036560596
    - name: Recall
      type: recall
      value: 0.32174364296834457
    - name: F1
      type: f1
      value: 0.3642773207990599
    - name: Accuracy
      type: accuracy
      value: 0.8502728197539998
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_100v7_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article100v7_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4325
- Precision: 0.4198
- Recall: 0.3217
- F1: 0.3643
- Accuracy: 0.8503

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
| No log        | 1.0   | 24   | 0.5750          | 0.1635    | 0.0267 | 0.0459 | 0.7926   |
| No log        | 2.0   | 48   | 0.4594          | 0.3845    | 0.2483 | 0.3017 | 0.8393   |
| No log        | 3.0   | 72   | 0.4325          | 0.4198    | 0.3217 | 0.3643 | 0.8503   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
