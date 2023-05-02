---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- clinc_oos
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased-distilled-clinc
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: clinc_oos
      type: clinc_oos
      args: plus
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9332258064516129
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: clinc_oos
      type: clinc_oos
      config: small
      split: test
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8587272727272727
      verified: true
    - name: Precision Macro
      type: precision
      value: 0.8619245385984416
      verified: true
    - name: Precision Micro
      type: precision
      value: 0.8587272727272727
      verified: true
    - name: Precision Weighted
      type: precision
      value: 0.8797945801452213
      verified: true
    - name: Recall Macro
      type: recall
      value: 0.9359690949227375
      verified: true
    - name: Recall Micro
      type: recall
      value: 0.8587272727272727
      verified: true
    - name: Recall Weighted
      type: recall
      value: 0.8587272727272727
      verified: true
    - name: F1 Macro
      type: f1
      value: 0.8922503214655346
      verified: true
    - name: F1 Micro
      type: f1
      value: 0.8587272727272727
      verified: true
    - name: F1 Weighted
      type: f1
      value: 0.8506829426037475
      verified: true
    - name: loss
      type: loss
      value: 0.9798759818077087
      verified: true
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-distilled-clinc

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the clinc_oos dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1259
- Accuracy: 0.9332

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
- train_batch_size: 48
- eval_batch_size: 48
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 7

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 318  | 0.5952          | 0.7355   |
| 0.7663        | 2.0   | 636  | 0.3130          | 0.8742   |
| 0.7663        | 3.0   | 954  | 0.2024          | 0.9206   |
| 0.3043        | 4.0   | 1272 | 0.1590          | 0.9235   |
| 0.181         | 5.0   | 1590 | 0.1378          | 0.9303   |
| 0.181         | 6.0   | 1908 | 0.1287          | 0.9329   |
| 0.1468        | 7.0   | 2226 | 0.1259          | 0.9332   |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0
