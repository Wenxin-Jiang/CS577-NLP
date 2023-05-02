---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article500v0_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_500v0_NER_Model_3Epochs_UNAUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article500v0_wikigold_split
      type: article500v0_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.6387981711299804
    - name: Recall
      type: recall
      value: 0.7249814677538917
    - name: F1
      type: f1
      value: 0.6791666666666667
    - name: Accuracy
      type: accuracy
      value: 0.9364674441205053
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_500v0_NER_Model_3Epochs_UNAUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article500v0_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1853
- Precision: 0.6388
- Recall: 0.7250
- F1: 0.6792
- Accuracy: 0.9365

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
| No log        | 1.0   | 59   | 0.2886          | 0.4480    | 0.6179 | 0.5194 | 0.9012   |
| No log        | 2.0   | 118  | 0.1912          | 0.6132    | 0.6946 | 0.6514 | 0.9327   |
| No log        | 3.0   | 177  | 0.1853          | 0.6388    | 0.7250 | 0.6792 | 0.9365   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
