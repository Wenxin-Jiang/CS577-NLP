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
- name: Article_500v0_NER_Model_3Epochs_AUGMENTED
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
      value: 0.7004528039010798
    - name: Recall
      type: recall
      value: 0.7453669384729429
    - name: F1
      type: f1
      value: 0.7222122463637995
    - name: Accuracy
      type: accuracy
      value: 0.9411139455782312
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_500v0_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article500v0_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2180
- Precision: 0.7005
- Recall: 0.7454
- F1: 0.7222
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
| No log        | 1.0   | 197  | 0.1988          | 0.6828    | 0.7046 | 0.6935 | 0.9347   |
| No log        | 2.0   | 394  | 0.2051          | 0.6942    | 0.7454 | 0.7189 | 0.9403   |
| 0.1447        | 3.0   | 591  | 0.2180          | 0.7005    | 0.7454 | 0.7222 | 0.9411   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
