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
- name: Article_500v6_NER_Model_3Epochs_UNAUGMENTED
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
      value: 0.6462295081967213
    - name: Recall
      type: recall
      value: 0.6930379746835443
    - name: F1
      type: f1
      value: 0.6688157448252461
    - name: Accuracy
      type: accuracy
      value: 0.9318540995006005
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_500v6_NER_Model_3Epochs_UNAUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article500v6_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2025
- Precision: 0.6462
- Recall: 0.6930
- F1: 0.6688
- Accuracy: 0.9319

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
| No log        | 1.0   | 63   | 0.2794          | 0.3775    | 0.4525 | 0.4116 | 0.8945   |
| No log        | 2.0   | 126  | 0.2119          | 0.6143    | 0.6670 | 0.6396 | 0.9266   |
| No log        | 3.0   | 189  | 0.2025          | 0.6462    | 0.6930 | 0.6688 | 0.9319   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
