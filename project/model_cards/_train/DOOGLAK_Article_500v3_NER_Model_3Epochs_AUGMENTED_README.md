---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article500v3_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_500v3_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article500v3_wikigold_split
      type: article500v3_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.7293136626042335
    - name: Recall
      type: recall
      value: 0.7574950033311126
    - name: F1
      type: f1
      value: 0.7431372549019608
    - name: Accuracy
      type: accuracy
      value: 0.9403332402494647
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_500v3_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article500v3_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2187
- Precision: 0.7293
- Recall: 0.7575
- F1: 0.7431
- Accuracy: 0.9403

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
| No log        | 1.0   | 187  | 0.2080          | 0.6933    | 0.7109 | 0.7020 | 0.9363   |
| No log        | 2.0   | 374  | 0.2159          | 0.7244    | 0.7338 | 0.7291 | 0.9379   |
| 0.1349        | 3.0   | 561  | 0.2187          | 0.7293    | 0.7575 | 0.7431 | 0.9403   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
