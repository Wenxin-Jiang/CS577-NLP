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
- name: hasoc19-bert-base-multilingual-uncased-sentiment-new
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hasoc19-bert-base-multilingual-uncased-sentiment-new

This model is a fine-tuned version of [bert-base-multilingual-uncased](https://huggingface.co/bert-base-multilingual-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4879
- Accuracy: 0.8433
- Precision: 0.8441
- Recall: 0.8433
- F1: 0.8436

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
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.4931        | 1.0   | 537  | 0.4011          | 0.8192   | 0.8212    | 0.8192 | 0.8198 |
| 0.3643        | 2.0   | 1074 | 0.4020          | 0.8291   | 0.8298    | 0.8291 | 0.8294 |
| 0.2816        | 3.0   | 1611 | 0.3837          | 0.8339   | 0.8378    | 0.8339 | 0.8347 |
| 0.2378        | 4.0   | 2148 | 0.4235          | 0.8381   | 0.8378    | 0.8381 | 0.8379 |
| 0.1904        | 5.0   | 2685 | 0.4753          | 0.8349   | 0.8350    | 0.8349 | 0.8349 |
| 0.1597        | 6.0   | 3222 | 0.4879          | 0.8433   | 0.8441    | 0.8433 | 0.8436 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
