---
license: cc-by-nc-sa-4.0
tags:
- generated_from_trainer
datasets:
- cord-layoutlmv3
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: layoutlmv3-finetuned-cord_100
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: cord-layoutlmv3
      type: cord-layoutlmv3
      config: cord
      split: train
      args: cord
    metrics:
    - name: Precision
      type: precision
      value: 0.9472118959107807
    - name: Recall
      type: recall
      value: 0.9535928143712575
    - name: F1
      type: f1
      value: 0.9503916449086163
    - name: Accuracy
      type: accuracy
      value: 0.9562818336162988
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutlmv3-finetuned-cord_100

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the cord-layoutlmv3 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2152
- Precision: 0.9472
- Recall: 0.9536
- F1: 0.9504
- Accuracy: 0.9563

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 5
- eval_batch_size: 5
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 2500

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.56  | 250  | 0.9909          | 0.7582    | 0.8099 | 0.7832 | 0.8128   |
| 1.3653        | 3.12  | 500  | 0.5650          | 0.8392    | 0.8675 | 0.8531 | 0.8756   |
| 1.3653        | 4.69  | 750  | 0.3851          | 0.8865    | 0.9177 | 0.9018 | 0.9181   |
| 0.3744        | 6.25  | 1000 | 0.3104          | 0.9280    | 0.9364 | 0.9322 | 0.9380   |
| 0.3744        | 7.81  | 1250 | 0.2778          | 0.9347    | 0.9424 | 0.9385 | 0.9440   |
| 0.1955        | 9.38  | 1500 | 0.2316          | 0.9327    | 0.9446 | 0.9386 | 0.9440   |
| 0.1955        | 10.94 | 1750 | 0.2461          | 0.9414    | 0.9491 | 0.9452 | 0.9533   |
| 0.1349        | 12.5  | 2000 | 0.2316          | 0.9379    | 0.9491 | 0.9435 | 0.9478   |
| 0.1349        | 14.06 | 2250 | 0.2227          | 0.9487    | 0.9551 | 0.9519 | 0.9533   |
| 0.1024        | 15.62 | 2500 | 0.2152          | 0.9472    | 0.9536 | 0.9504 | 0.9563   |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
