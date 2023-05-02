---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imdb
metrics:
- accuracy
- f1
model-index:
- name: sentiment-model-on-imdb-dataset
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: imdb
      type: imdb
      config: plain_text
      split: train
      args: plain_text
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.85
    - name: F1
      type: f1
      value: 0.8543689320388349
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sentiment-model-on-imdb-dataset

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the imdb dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3694
- Accuracy: 0.85
- F1: 0.8544

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results



### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
