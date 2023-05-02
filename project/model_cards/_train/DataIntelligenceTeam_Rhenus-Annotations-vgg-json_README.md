---
license: cc-by-nc-sa-4.0
tags:
- generated_from_trainer
datasets:
- dataset
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Rhenus-Annotations-vgg-json
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: dataset
      type: dataset
      config: funsd
      split: train
      args: funsd
    metrics:
    - name: Precision
      type: precision
      value: 0.989247311827957
    - name: Recall
      type: recall
      value: 0.9633507853403142
    - name: F1
      type: f1
      value: 0.9761273209549071
    - name: Accuracy
      type: accuracy
      value: 0.5833333333333334
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Rhenus-Annotations-vgg-json

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 3.3432
- Precision: 0.9892
- Recall: 0.9634
- F1: 0.9761
- Accuracy: 0.5833

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
- training_steps: 2000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 2.5   | 100  | 2.4965          | 0.9255    | 0.9110 | 0.9182 | 0.5637   |
| No log        | 5.0   | 200  | 2.7204          | 0.9838    | 0.9529 | 0.9681 | 0.5752   |
| No log        | 7.5   | 300  | 3.0295          | 0.9892    | 0.9634 | 0.9761 | 0.5833   |
| No log        | 10.0  | 400  | 3.1623          | 0.9892    | 0.9634 | 0.9761 | 0.5833   |
| 0.4467        | 12.5  | 500  | 3.3432          | 0.9892    | 0.9634 | 0.9761 | 0.5833   |
| 0.4467        | 15.0  | 600  | 3.4314          | 0.9892    | 0.9634 | 0.9761 | 0.5833   |
| 0.4467        | 17.5  | 700  | 3.5995          | 0.9892    | 0.9634 | 0.9761 | 0.5833   |
| 0.4467        | 20.0  | 800  | 3.6942          | 0.9892    | 0.9634 | 0.9761 | 0.5833   |
| 0.4467        | 22.5  | 900  | 3.7672          | 0.9892    | 0.9634 | 0.9761 | 0.5833   |
| 0.1072        | 25.0  | 1000 | 3.8307          | 0.9892    | 0.9634 | 0.9761 | 0.5833   |
| 0.1072        | 27.5  | 1100 | 3.9029          | 0.9786    | 0.9581 | 0.9683 | 0.5822   |
| 0.1072        | 30.0  | 1200 | 3.9604          | 0.9892    | 0.9634 | 0.9761 | 0.5833   |
| 0.1072        | 32.5  | 1300 | 4.0041          | 0.9892    | 0.9634 | 0.9761 | 0.5833   |
| 0.1072        | 35.0  | 1400 | 4.0384          | 0.9892    | 0.9634 | 0.9761 | 0.5833   |
| 0.0426        | 37.5  | 1500 | 4.0769          | 0.9892    | 0.9634 | 0.9761 | 0.5833   |
| 0.0426        | 40.0  | 1600 | 4.0993          | 0.9892    | 0.9634 | 0.9761 | 0.5833   |
| 0.0426        | 42.5  | 1700 | 4.1221          | 0.9892    | 0.9634 | 0.9761 | 0.5833   |
| 0.0426        | 45.0  | 1800 | 4.1346          | 0.9892    | 0.9634 | 0.9761 | 0.5833   |
| 0.0426        | 47.5  | 1900 | 4.1458          | 0.9892    | 0.9634 | 0.9761 | 0.5833   |
| 0.0205        | 50.0  | 2000 | 4.1482          | 0.9892    | 0.9634 | 0.9761 | 0.5833   |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
