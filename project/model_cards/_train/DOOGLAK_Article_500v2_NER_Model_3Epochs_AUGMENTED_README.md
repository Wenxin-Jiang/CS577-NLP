---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article500v2_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_500v2_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article500v2_wikigold_split
      type: article500v2_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.7113220815752461
    - name: Recall
      type: recall
      value: 0.7526041666666666
    - name: F1
      type: f1
      value: 0.7313810556760665
    - name: Accuracy
      type: accuracy
      value: 0.9410548086866598
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_500v2_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article500v2_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2086
- Precision: 0.7113
- Recall: 0.7526
- F1: 0.7314
- Accuracy: 0.9411

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
| No log        | 1.0   | 185  | 0.1795          | 0.6982    | 0.7530 | 0.7245 | 0.9412   |
| No log        | 2.0   | 370  | 0.2018          | 0.7218    | 0.7537 | 0.7374 | 0.9403   |
| 0.1342        | 3.0   | 555  | 0.2086          | 0.7113    | 0.7526 | 0.7314 | 0.9411   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
