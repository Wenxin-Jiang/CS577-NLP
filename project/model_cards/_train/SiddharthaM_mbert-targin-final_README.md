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
- name: mbert-targin-final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbert-targin-final

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9847
- Accuracy: 0.7025
- Precision: 0.6490
- Recall: 0.6487
- F1: 0.6489

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
| No log        | 1.0   | 296  | 0.5774          | 0.7091   | 0.6506    | 0.6378 | 0.6426 |
| 0.5912        | 2.0   | 592  | 0.5316          | 0.7376   | 0.6880    | 0.6767 | 0.6814 |
| 0.5912        | 3.0   | 888  | 0.5511          | 0.7253   | 0.6692    | 0.6293 | 0.6378 |
| 0.4844        | 4.0   | 1184 | 0.6262          | 0.6835   | 0.6622    | 0.6884 | 0.6613 |
| 0.4844        | 5.0   | 1480 | 0.6320          | 0.7006   | 0.6574    | 0.6701 | 0.6616 |
| 0.3861        | 6.0   | 1776 | 0.6983          | 0.7148   | 0.6632    | 0.6620 | 0.6626 |
| 0.2773        | 7.0   | 2072 | 0.8109          | 0.7110   | 0.6630    | 0.6689 | 0.6655 |
| 0.2773        | 8.0   | 2368 | 0.8948          | 0.7072   | 0.6525    | 0.6487 | 0.6504 |
| 0.2068        | 9.0   | 2664 | 0.9693          | 0.7072   | 0.6519    | 0.6469 | 0.6492 |
| 0.2068        | 10.0  | 2960 | 0.9847          | 0.7025   | 0.6490    | 0.6487 | 0.6489 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
