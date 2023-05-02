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
- name: model_from_berturk_1401_v3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# model_from_berturk_1401_v3

This model is a fine-tuned version of [dbmdz/bert-base-turkish-cased](https://huggingface.co/dbmdz/bert-base-turkish-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4042
- Precision: 0.8896
- Recall: 0.8841
- F1: 0.8868
- Accuracy: 0.9198

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
| No log        | 1.0   | 244  | 0.3948          | 0.8565    | 0.8508 | 0.8536 | 0.8932   |
| No log        | 2.0   | 488  | 0.3331          | 0.8724    | 0.8663 | 0.8693 | 0.9060   |
| 0.6019        | 3.0   | 732  | 0.3061          | 0.8855    | 0.8746 | 0.8800 | 0.9147   |
| 0.6019        | 4.0   | 976  | 0.3025          | 0.8881    | 0.8828 | 0.8855 | 0.9177   |
| 0.2753        | 5.0   | 1220 | 0.3137          | 0.8807    | 0.8819 | 0.8813 | 0.9148   |
| 0.2753        | 6.0   | 1464 | 0.3140          | 0.8876    | 0.8854 | 0.8865 | 0.9178   |
| 0.1963        | 7.0   | 1708 | 0.3210          | 0.8871    | 0.8840 | 0.8855 | 0.9182   |
| 0.1963        | 8.0   | 1952 | 0.3304          | 0.8908    | 0.8855 | 0.8882 | 0.9208   |
| 0.1431        | 9.0   | 2196 | 0.3452          | 0.8907    | 0.8843 | 0.8875 | 0.9206   |
| 0.1431        | 10.0  | 2440 | 0.3584          | 0.8896    | 0.8835 | 0.8865 | 0.9201   |
| 0.1061        | 11.0  | 2684 | 0.3770          | 0.8883    | 0.8849 | 0.8866 | 0.9191   |
| 0.1061        | 12.0  | 2928 | 0.3852          | 0.8876    | 0.8834 | 0.8855 | 0.9186   |
| 0.082         | 13.0  | 3172 | 0.3941          | 0.8894    | 0.8833 | 0.8863 | 0.9195   |
| 0.082         | 14.0  | 3416 | 0.3973          | 0.8893    | 0.8842 | 0.8867 | 0.9197   |
| 0.0694        | 15.0  | 3660 | 0.4042          | 0.8896    | 0.8841 | 0.8868 | 0.9198   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
