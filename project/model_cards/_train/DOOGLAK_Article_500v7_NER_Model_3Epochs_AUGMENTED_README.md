---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article500v7_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_500v7_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article500v7_wikigold_split
      type: article500v7_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.7235232436211115
    - name: Recall
      type: recall
      value: 0.7613093048915043
    - name: F1
      type: f1
      value: 0.7419354838709679
    - name: Accuracy
      type: accuracy
      value: 0.9419641450581304
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_500v7_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article500v7_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1961
- Precision: 0.7235
- Recall: 0.7613
- F1: 0.7419
- Accuracy: 0.9420

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
| No log        | 1.0   | 162  | 0.1924          | 0.6942    | 0.7087 | 0.7014 | 0.9358   |
| No log        | 2.0   | 324  | 0.1958          | 0.7165    | 0.7540 | 0.7348 | 0.9403   |
| No log        | 3.0   | 486  | 0.1961          | 0.7235    | 0.7613 | 0.7419 | 0.9420   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
