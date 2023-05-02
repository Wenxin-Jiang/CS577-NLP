---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- recall
- precision
model-index:
- name: distilbert-bbc-news-classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-bbc-news-classification

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0669
- Accuracy: 0.9880
- F1-score: 0.9880
- Recall: 0.9886
- Precision: 0.9875

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1-score | Recall | Precision |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|:------:|:---------:|
| No log        | 1.0   | 98   | 0.1495          | 0.9775   | 0.9775   | 0.9772 | 0.9781    |
| No log        | 2.0   | 196  | 0.0737          | 0.9880   | 0.9882   | 0.9885 | 0.9880    |
| No log        | 3.0   | 294  | 0.0669          | 0.9880   | 0.9880   | 0.9886 | 0.9875    |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
