---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article500v5_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_500v5_NER_Model_3Epochs_UNAUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article500v5_wikigold_split
      type: article500v5_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.6407736207989854
    - name: Recall
      type: recall
      value: 0.7217857142857143
    - name: F1
      type: f1
      value: 0.6788713469936176
    - name: Accuracy
      type: accuracy
      value: 0.9355859657583796
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_500v5_NER_Model_3Epochs_UNAUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article500v5_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1914
- Precision: 0.6408
- Recall: 0.7218
- F1: 0.6789
- Accuracy: 0.9356

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
| No log        | 1.0   | 56   | 0.2937          | 0.4307    | 0.5257 | 0.4735 | 0.9010   |
| No log        | 2.0   | 112  | 0.2037          | 0.6089    | 0.695  | 0.6491 | 0.9305   |
| No log        | 3.0   | 168  | 0.1914          | 0.6408    | 0.7218 | 0.6789 | 0.9356   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
