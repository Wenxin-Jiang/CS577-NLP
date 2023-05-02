---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wnut_17
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: distilbert-base-uncased-test2
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wnut_17
      type: wnut_17
      config: wnut_17
      split: train
      args: wnut_17
    metrics:
    - name: Precision
      type: precision
      value: 0.5278121137206427
    - name: Recall
      type: recall
      value: 0.3957367933271548
    - name: F1
      type: f1
      value: 0.4523305084745763
    - name: Accuracy
      type: accuracy
      value: 0.9461758796118165
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-test2

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the wnut_17 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3055
- Precision: 0.5278
- Recall: 0.3957
- F1: 0.4523
- Accuracy: 0.9462

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
| No log        | 1.0   | 213  | 0.2889          | 0.5439    | 0.3503 | 0.4262 | 0.9453   |
| No log        | 2.0   | 426  | 0.2938          | 0.5236    | 0.3800 | 0.4404 | 0.9457   |
| 0.0544        | 3.0   | 639  | 0.3055          | 0.5278    | 0.3957 | 0.4523 | 0.9462   |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu102
- Datasets 2.4.0
- Tokenizers 0.12.1
