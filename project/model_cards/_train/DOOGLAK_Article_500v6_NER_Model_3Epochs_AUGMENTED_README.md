---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article500v6_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_500v6_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article500v6_wikigold_split
      type: article500v6_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.7276069518716578
    - name: Recall
      type: recall
      value: 0.7654711673699015
    - name: F1
      type: f1
      value: 0.7460589444825222
    - name: Accuracy
      type: accuracy
      value: 0.944971237119919
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_500v6_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article500v6_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2052
- Precision: 0.7276
- Recall: 0.7655
- F1: 0.7461
- Accuracy: 0.9450

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
| No log        | 1.0   | 209  | 0.1846          | 0.7211    | 0.7472 | 0.7339 | 0.9434   |
| No log        | 2.0   | 418  | 0.2111          | 0.7114    | 0.7384 | 0.7246 | 0.9410   |
| 0.1368        | 3.0   | 627  | 0.2052          | 0.7276    | 0.7655 | 0.7461 | 0.9450   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
