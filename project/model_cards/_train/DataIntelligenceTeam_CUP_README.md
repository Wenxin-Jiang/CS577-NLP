---
license: cc-by-nc-sa-4.0
tags:
- generated_from_trainer
datasets:
- sroie
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: CUP
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: sroie
      type: sroie
      config: discharge
      split: test
      args: discharge
    metrics:
    - name: Precision
      type: precision
      value: 0.9674418604651163
    - name: Recall
      type: recall
      value: 0.9952153110047847
    - name: F1
      type: f1
      value: 0.981132075471698
    - name: Accuracy
      type: accuracy
      value: 0.9977973568281938
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CUP

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the sroie dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0166
- Precision: 0.9674
- Recall: 0.9952
- F1: 0.9811
- Accuracy: 0.9978

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 1000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.47  | 100  | 0.0258          | 0.8851    | 0.9952 | 0.9369 | 0.9905   |
| No log        | 2.94  | 200  | 0.0183          | 0.92      | 0.9904 | 0.9539 | 0.9941   |
| No log        | 4.41  | 300  | 0.0143          | 0.9674    | 0.9952 | 0.9811 | 0.9978   |
| No log        | 5.88  | 400  | 0.0166          | 0.9498    | 0.9952 | 0.9720 | 0.9963   |
| 0.0211        | 7.35  | 500  | 0.0179          | 0.9412    | 0.9952 | 0.9674 | 0.9956   |
| 0.0211        | 8.82  | 600  | 0.0161          | 0.9674    | 0.9952 | 0.9811 | 0.9978   |
| 0.0211        | 10.29 | 700  | 0.0168          | 0.9674    | 0.9952 | 0.9811 | 0.9978   |
| 0.0211        | 11.76 | 800  | 0.0168          | 0.9674    | 0.9952 | 0.9811 | 0.9978   |
| 0.0211        | 13.24 | 900  | 0.0170          | 0.9674    | 0.9952 | 0.9811 | 0.9978   |
| 0.0003        | 14.71 | 1000 | 0.0166          | 0.9674    | 0.9952 | 0.9811 | 0.9978   |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu116
- Datasets 2.2.2
- Tokenizers 0.13.2
