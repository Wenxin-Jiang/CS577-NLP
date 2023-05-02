---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy, F1 Score
model-index:
- name: distilbert-base-uncased-Financial_Sentiment_Analysis
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-Finanacial_Sentiment_Analysis

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3079
- Accuracy: 0.8529
- F1 Score: 0.8564

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1 Score |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| 0.5569        | 1.0   | 134  | 0.3954          | 0.7591   | 0.7559   |
| 0.3177        | 2.0   | 268  | 0.3391          | 0.8135   | 0.8151   |
| 0.2479        | 3.0   | 402  | 0.3211          | 0.8322   | 0.8353   |
| 0.2049        | 4.0   | 536  | 0.3066          | 0.8463   | 0.8506   |
| 0.1802        | 5.0   | 670  | 0.3079          | 0.8529   | 0.8564   |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
