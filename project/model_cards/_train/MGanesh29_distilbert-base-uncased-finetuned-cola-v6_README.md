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
- name: distilbert-base-uncased-finetuned-cola-v6
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-cola-v6

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4210
- Accuracy: 0.9310
- Precision: 0.9310
- Recall: 0.9310
- F1: 0.9310

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 6.25  | 50   | 1.2900          | 0.5862   | 0.5862    | 0.5862 | 0.5862 |
| No log        | 12.5  | 100  | 0.6947          | 0.8621   | 0.8621    | 0.8621 | 0.8621 |
| No log        | 18.75 | 150  | 0.4672          | 0.9310   | 0.9310    | 0.9310 | 0.9310 |
| No log        | 25.0  | 200  | 0.4265          | 0.9310   | 0.9310    | 0.9310 | 0.9310 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
