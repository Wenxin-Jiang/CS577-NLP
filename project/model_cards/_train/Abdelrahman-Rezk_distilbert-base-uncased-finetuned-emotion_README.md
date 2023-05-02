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
      value: 0.8885
    - name: F1
      type: f1
      value: 0.8818845305609924
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
      value: 0.892
      verified: true
    - name: Precision Macro
      type: precision
      value: 0.8923475194643138
      verified: true
    - name: Precision Micro
      type: precision
      value: 0.892
      verified: true
    - name: Precision Weighted
      type: precision
      value: 0.894495118514709
      verified: true
    - name: Recall Macro
      type: recall
      value: 0.768240931585822
      verified: true
    - name: Recall Micro
      type: recall
      value: 0.892
      verified: true
    - name: Recall Weighted
      type: recall
      value: 0.892
      verified: true
    - name: F1 Macro
      type: f1
      value: 0.7897026729904524
      verified: true
    - name: F1 Micro
      type: f1
      value: 0.892
      verified: true
    - name: F1 Weighted
      type: f1
      value: 0.8842367889371163
      verified: true
    - name: loss
      type: loss
      value: 0.34626322984695435
      verified: true
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: emotion
      type: emotion
      config: default
      split: validation
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8885
      verified: true
    - name: Precision Macro
      type: precision
      value: 0.8849064522901132
      verified: true
    - name: Precision Micro
      type: precision
      value: 0.8885
      verified: true
    - name: Precision Weighted
      type: precision
      value: 0.8922726271705158
      verified: true
    - name: Recall Macro
      type: recall
      value: 0.7854833401719518
      verified: true
    - name: Recall Micro
      type: recall
      value: 0.8885
      verified: true
    - name: Recall Weighted
      type: recall
      value: 0.8885
      verified: true
    - name: F1 Macro
      type: f1
      value: 0.8031492596189961
      verified: true
    - name: F1 Micro
      type: f1
      value: 0.8885
      verified: true
    - name: F1 Weighted
      type: f1
      value: 0.8818845305609924
      verified: true
    - name: loss
      type: loss
      value: 0.36373236775398254
      verified: true
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-emotion

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the emotion dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3663
- Accuracy: 0.8885
- F1: 0.8819

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
- train_batch_size: 128
- eval_batch_size: 128
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| No log        | 1.0   | 125  | 0.5574          | 0.822    | 0.7956 |
| 0.7483        | 2.0   | 250  | 0.3663          | 0.8885   | 0.8819 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.1+cu111
- Datasets 2.1.0
- Tokenizers 0.12.1
