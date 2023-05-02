---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article500v8_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_500v8_NER_Model_3Epochs_UNAUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article500v8_wikigold_split
      type: article500v8_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.6780405405405405
    - name: Recall
      type: recall
      value: 0.7117021276595744
    - name: F1
      type: f1
      value: 0.6944636678200693
    - name: Accuracy
      type: accuracy
      value: 0.9363021063950914
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_500v8_NER_Model_3Epochs_UNAUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article500v8_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1980
- Precision: 0.6780
- Recall: 0.7117
- F1: 0.6945
- Accuracy: 0.9363

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
| No log        | 1.0   | 64   | 0.2758          | 0.5405    | 0.5298 | 0.5351 | 0.9135   |
| No log        | 2.0   | 128  | 0.2129          | 0.6350    | 0.6695 | 0.6518 | 0.9296   |
| No log        | 3.0   | 192  | 0.1980          | 0.6780    | 0.7117 | 0.6945 | 0.9363   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
