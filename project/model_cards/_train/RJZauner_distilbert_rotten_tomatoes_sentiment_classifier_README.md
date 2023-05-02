---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- rotten_tomatoes
metrics:
- accuracy
model-index:
- name: outputs
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: rotten_tomatoes
      type: rotten_tomatoes
      config: default
      split: train
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8386491557223265
---

# distilbert_rotten_tomatoes_sentiment_classifier

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the rotten_tomatoes dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7927
- Accuracy: 0.8386

## Model description

The goal was to fine-tune a model on the rotten_tomatoes dataset to showcase an end-to-end workflow using the Hugging face library. As such, only the bare minimum  of pre-processing was used.

## Intended uses & limitations

The model will be used as part of a blog post to help others engineers better understand what natural language processing is and how to perform a text classification.

## Training and evaluation data

The model was evaluated using the accuracy metric that form part of the Hugging Face library.

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 134  | 0.5940          | 0.8340   |
| No log        | 2.0   | 268  | 0.7095          | 0.8227   |
| No log        | 3.0   | 402  | 0.7276          | 0.8321   |
| 0.065         | 4.0   | 536  | 0.7693          | 0.8415   |
| 0.065         | 5.0   | 670  | 0.7927          | 0.8386   |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
