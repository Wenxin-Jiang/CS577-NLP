---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article250v1_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_250v1_NER_Model_3Epochs_UNAUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article250v1_wikigold_split
      type: article250v1_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.46870653685674546
    - name: Recall
      type: recall
      value: 0.47571993224167136
    - name: F1
      type: f1
      value: 0.47218719349866894
    - name: Accuracy
      type: accuracy
      value: 0.9010771263083021
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_250v1_NER_Model_3Epochs_UNAUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article250v1_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2871
- Precision: 0.4687
- Recall: 0.4757
- F1: 0.4722
- Accuracy: 0.9011

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
| No log        | 1.0   | 31   | 0.4885          | 0.1689    | 0.0426 | 0.0681 | 0.8016   |
| No log        | 2.0   | 62   | 0.3231          | 0.3894    | 0.3834 | 0.3864 | 0.8874   |
| No log        | 3.0   | 93   | 0.2871          | 0.4687    | 0.4757 | 0.4722 | 0.9011   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
