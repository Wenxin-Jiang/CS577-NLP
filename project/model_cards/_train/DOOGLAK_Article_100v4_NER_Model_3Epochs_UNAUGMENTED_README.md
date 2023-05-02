---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article100v4_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_100v4_NER_Model_3Epochs_UNAUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article100v4_wikigold_split
      type: article100v4_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.16216216216216217
    - name: Recall
      type: recall
      value: 0.0030761343245321714
    - name: F1
      type: f1
      value: 0.006037735849056605
    - name: Accuracy
      type: accuracy
      value: 0.7826991539137269
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_100v4_NER_Model_3Epochs_UNAUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article100v4_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5862
- Precision: 0.1622
- Recall: 0.0031
- F1: 0.0060
- Accuracy: 0.7827

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
| No log        | 1.0   | 12   | 0.7284          | 0.0       | 0.0    | 0.0    | 0.7816   |
| No log        | 2.0   | 24   | 0.6227          | 0.2       | 0.0003 | 0.0005 | 0.7817   |
| No log        | 3.0   | 36   | 0.5862          | 0.1622    | 0.0031 | 0.0060 | 0.7827   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6