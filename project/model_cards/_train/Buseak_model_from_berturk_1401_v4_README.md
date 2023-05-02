---
license: mit
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: model_from_berturk_1401_v4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# model_from_berturk_1401_v4

This model is a fine-tuned version of [Buseak/model_from_berturk_1401_v3](https://huggingface.co/Buseak/model_from_berturk_1401_v3) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0070
- Precision: 0.9983
- Recall: 0.9981
- F1: 0.9982
- Accuracy: 0.9985

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 244  | 0.1500          | 0.9425    | 0.9362 | 0.9393 | 0.9575   |
| No log        | 2.0   | 488  | 0.1115          | 0.9570    | 0.9519 | 0.9544 | 0.9681   |
| 0.1776        | 3.0   | 732  | 0.0801          | 0.9700    | 0.9665 | 0.9683 | 0.9774   |
| 0.1776        | 4.0   | 976  | 0.0577          | 0.9792    | 0.9772 | 0.9782 | 0.9841   |
| 0.1024        | 5.0   | 1220 | 0.0490          | 0.9818    | 0.9809 | 0.9814 | 0.9866   |
| 0.1024        | 6.0   | 1464 | 0.0346          | 0.9882    | 0.9864 | 0.9873 | 0.9907   |
| 0.0901        | 7.0   | 1708 | 0.0254          | 0.9920    | 0.9910 | 0.9915 | 0.9935   |
| 0.0901        | 8.0   | 1952 | 0.0205          | 0.9935    | 0.9922 | 0.9928 | 0.9947   |
| 0.0617        | 9.0   | 2196 | 0.0157          | 0.9954    | 0.9947 | 0.9951 | 0.9963   |
| 0.0617        | 10.0  | 2440 | 0.0126          | 0.9965    | 0.9959 | 0.9962 | 0.9970   |
| 0.0438        | 11.0  | 2684 | 0.0110          | 0.9969    | 0.9965 | 0.9967 | 0.9975   |
| 0.0438        | 12.0  | 2928 | 0.0091          | 0.9976    | 0.9974 | 0.9975 | 0.9980   |
| 0.033         | 13.0  | 3172 | 0.0080          | 0.9979    | 0.9977 | 0.9978 | 0.9982   |
| 0.033         | 14.0  | 3416 | 0.0073          | 0.9982    | 0.9979 | 0.9981 | 0.9984   |
| 0.0264        | 15.0  | 3660 | 0.0070          | 0.9983    | 0.9981 | 0.9982 | 0.9985   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
