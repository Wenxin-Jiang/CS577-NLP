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
- name: distilbert-profane-final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-profane-final

This model is a fine-tuned version of [distilbert-base-multilingual-cased](https://huggingface.co/distilbert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2773
- Accuracy: 0.8992
- Precision: 0.8261
- Recall: 0.7987
- F1: 0.8114

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 1.0   | 296  | 0.2862          | 0.8907   | 0.8230    | 0.7528 | 0.7807 |
| 0.3379        | 2.0   | 592  | 0.2650          | 0.9097   | 0.8748    | 0.7778 | 0.8148 |
| 0.3379        | 3.0   | 888  | 0.2632          | 0.9049   | 0.8417    | 0.7999 | 0.8185 |
| 0.221         | 4.0   | 1184 | 0.2772          | 0.8916   | 0.8055    | 0.8055 | 0.8055 |
| 0.221         | 5.0   | 1480 | 0.2773          | 0.8992   | 0.8261    | 0.7987 | 0.8114 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
