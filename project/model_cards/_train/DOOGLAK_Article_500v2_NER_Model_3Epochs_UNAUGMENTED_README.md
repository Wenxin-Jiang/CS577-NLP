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
- name: Article_500v2_NER_Model_3Epochs_UNAUGMENTED
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
      value: 0.6510177281680893
    - name: Recall
      type: recall
      value: 0.7377232142857143
    - name: F1
      type: f1
      value: 0.6916637600279038
    - name: Accuracy
      type: accuracy
      value: 0.936698943937827
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_500v2_NER_Model_3Epochs_UNAUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article500v2_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1886
- Precision: 0.6510
- Recall: 0.7377
- F1: 0.6917
- Accuracy: 0.9367

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
| No log        | 1.0   | 62   | 0.2863          | 0.4448    | 0.5990 | 0.5105 | 0.8927   |
| No log        | 2.0   | 124  | 0.1965          | 0.6070    | 0.7321 | 0.6637 | 0.9308   |
| No log        | 3.0   | 186  | 0.1886          | 0.6510    | 0.7377 | 0.6917 | 0.9367   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
