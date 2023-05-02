---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tsl_news
metrics:
- accuracy
- f1
model-index:
- name: news-tsl-train
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: tsl_news
      type: tsl_news
      config: plain_text
      split: train
      args: plain_text
    metrics:
    - name: Accuracy
      type: accuracy
      value: 1.0
    - name: F1
      type: f1
      value: 1.0
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# news-tsl-train

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the tsl_news dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0125
- Accuracy: 1.0
- F1: 1.0

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
- num_epochs: 10

### Training results



### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.2
- Tokenizers 0.12.1
