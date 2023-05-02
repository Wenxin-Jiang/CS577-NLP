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
- name: hasoc19-bert-base-multilingual-cased-profane-new
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hasoc19-bert-base-multilingual-cased-profane-new

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5065
- Accuracy: 0.9030
- Precision: 0.8465
- Recall: 0.8330
- F1: 0.8395

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
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 1.0   | 296  | 0.2873          | 0.8954   | 0.8513    | 0.7881 | 0.8140 |
| 0.2999        | 2.0   | 592  | 0.2556          | 0.9078   | 0.8703    | 0.8149 | 0.8385 |
| 0.2999        | 3.0   | 888  | 0.2595          | 0.9106   | 0.8613    | 0.8415 | 0.8509 |
| 0.1945        | 4.0   | 1184 | 0.2682          | 0.9078   | 0.8601    | 0.8302 | 0.8439 |
| 0.1945        | 5.0   | 1480 | 0.3286          | 0.9087   | 0.8590    | 0.8365 | 0.8471 |
| 0.142         | 6.0   | 1776 | 0.3911          | 0.9002   | 0.8390    | 0.8351 | 0.8370 |
| 0.0944        | 7.0   | 2072 | 0.4184          | 0.9068   | 0.8558    | 0.8334 | 0.8439 |
| 0.0944        | 8.0   | 2368 | 0.4763          | 0.9011   | 0.8450    | 0.8261 | 0.8350 |
| 0.0631        | 9.0   | 2664 | 0.4952          | 0.9002   | 0.8412    | 0.8293 | 0.8351 |
| 0.0631        | 10.0  | 2960 | 0.5065          | 0.9030   | 0.8465    | 0.8330 | 0.8395 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
