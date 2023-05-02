---
tags:
- generated_from_trainer
datasets:
- conll2003
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: rubert-tiny2-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      config: conll2003
      split: train
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.7137235200535879
    - name: Recall
      type: recall
      value: 0.7270556124189697
    - name: F1
      type: f1
      value: 0.7203278827058774
    - name: Accuracy
      type: accuracy
      value: 0.9363443855435385
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# rubert-tiny2-finetuned-ner

This model was trained from scratch on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2259
- Precision: 0.7137
- Recall: 0.7271
- F1: 0.7203
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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.6327        | 1.0   | 878  | 0.3218          | 0.6068    | 0.6009 | 0.6038 | 0.9114   |
| 0.2937        | 2.0   | 1756 | 0.2434          | 0.6864    | 0.7013 | 0.6938 | 0.9307   |
| 0.2357        | 3.0   | 2634 | 0.2259          | 0.7137    | 0.7271 | 0.7203 | 0.9363   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
