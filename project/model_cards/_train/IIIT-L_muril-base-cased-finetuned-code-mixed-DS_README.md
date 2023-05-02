---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: muril-base-cased-finetuned-code-mixed-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# muril-base-cased-finetuned-code-mixed-DS

This model is a fine-tuned version of [google/muril-base-cased](https://huggingface.co/google/muril-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9319
- Accuracy: 0.6982
- Precision: 0.6327
- Recall: 0.6314
- F1: 0.6320

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 25

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0542        | 1.98  | 248  | 0.9786          | 0.5976   | 0.3936    | 0.5454 | 0.4330 |
| 0.9307        | 3.97  | 496  | 0.8836          | 0.5996   | 0.4072    | 0.5604 | 0.4399 |
| 0.8323        | 5.95  | 744  | 0.8266          | 0.5996   | 0.5508    | 0.5720 | 0.4527 |
| 0.7554        | 7.94  | 992  | 0.8006          | 0.6318   | 0.5601    | 0.5838 | 0.5232 |
| 0.6821        | 9.92  | 1240 | 0.8777          | 0.6740   | 0.5929    | 0.5875 | 0.5836 |
| 0.6173        | 11.9  | 1488 | 0.8389          | 0.6640   | 0.5918    | 0.6031 | 0.5881 |
| 0.5552        | 13.89 | 1736 | 0.9003          | 0.6962   | 0.6240    | 0.6160 | 0.6191 |
| 0.4932        | 15.87 | 1984 | 0.8979          | 0.6982   | 0.6266    | 0.6231 | 0.6245 |
| 0.4446        | 17.86 | 2232 | 0.9104          | 0.7002   | 0.6310    | 0.6290 | 0.6298 |
| 0.4084        | 19.84 | 2480 | 0.9284          | 0.7002   | 0.6278    | 0.6255 | 0.6264 |
| 0.3763        | 21.82 | 2728 | 0.9228          | 0.7082   | 0.6436    | 0.6380 | 0.6398 |
| 0.3575        | 23.81 | 2976 | 0.9319          | 0.6982   | 0.6327    | 0.6314 | 0.6320 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1
