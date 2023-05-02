---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- emotion
metrics:
- accuracy
- f1
model-index:
- name: distilbert-base-uncased-finetuned-emotion
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: emotion
      type: emotion
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.937
    - name: F1
      type: f1
      value: 0.9372331942198677
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: emotion
      type: emotion
      config: default
      split: test
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.924
      verified: true
    - name: Precision Macro
      type: precision
      value: 0.8811256547088461
      verified: true
    - name: Precision Micro
      type: precision
      value: 0.924
      verified: true
    - name: Precision Weighted
      type: precision
      value: 0.9250809835160841
      verified: true
    - name: Recall Macro
      type: recall
      value: 0.8882276452967225
      verified: true
    - name: Recall Micro
      type: recall
      value: 0.924
      verified: true
    - name: Recall Weighted
      type: recall
      value: 0.924
      verified: true
    - name: F1 Macro
      type: f1
      value: 0.8844059421244559
      verified: true
    - name: F1 Micro
      type: f1
      value: 0.924
      verified: true
    - name: F1 Weighted
      type: f1
      value: 0.9243911585312775
      verified: true
    - name: loss
      type: loss
      value: 0.15944455564022064
      verified: true
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-emotion

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the emotion dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1413
- Accuracy: 0.937
- F1: 0.9372

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.7628        | 1.0   | 250  | 0.2489          | 0.9155   | 0.9141 |
| 0.2014        | 2.0   | 500  | 0.1716          | 0.928    | 0.9283 |
| 0.1351        | 3.0   | 750  | 0.1456          | 0.937    | 0.9374 |
| 0.1046        | 4.0   | 1000 | 0.1440          | 0.9355   | 0.9349 |
| 0.0877        | 5.0   | 1250 | 0.1413          | 0.937    | 0.9372 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
