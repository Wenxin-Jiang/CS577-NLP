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
- name: mbert-profane-final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbert-profane-final

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4464
- Accuracy: 0.8983
- Precision: 0.8135
- Recall: 0.8120
- F1: 0.8128

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
| No log        | 1.0   | 296  | 0.2313          | 0.9154   | 0.8687    | 0.8010 | 0.8294 |
| 0.3077        | 2.0   | 592  | 0.2223          | 0.9125   | 0.8473    | 0.8205 | 0.8330 |
| 0.3077        | 3.0   | 888  | 0.2137          | 0.9259   | 0.8784    | 0.8379 | 0.8563 |
| 0.2102        | 4.0   | 1184 | 0.2334          | 0.9163   | 0.8483    | 0.8417 | 0.8449 |
| 0.2102        | 5.0   | 1480 | 0.2737          | 0.9068   | 0.8305    | 0.8242 | 0.8273 |
| 0.1533        | 6.0   | 1776 | 0.3214          | 0.8964   | 0.8034    | 0.8510 | 0.8239 |
| 0.1092        | 7.0   | 2072 | 0.3409          | 0.9002   | 0.8115    | 0.8414 | 0.8252 |
| 0.1092        | 8.0   | 2368 | 0.3849          | 0.9049   | 0.8322    | 0.8066 | 0.8185 |
| 0.0775        | 9.0   | 2664 | 0.4408          | 0.8983   | 0.8113    | 0.8215 | 0.8162 |
| 0.0775        | 10.0  | 2960 | 0.4464          | 0.8983   | 0.8135    | 0.8120 | 0.8128 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
