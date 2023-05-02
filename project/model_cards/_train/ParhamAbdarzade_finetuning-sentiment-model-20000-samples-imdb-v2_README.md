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
- name: finetuning-sentiment-model-20000-samples-imdb-v2
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
      value: 0.924
    - name: F1
      type: f1
      value: 0.9241516966067864
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuning-sentiment-model-20000-samples-imdb-v2

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the imdb dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3694
- Accuracy: 0.924
- F1: 0.9242

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.2795        | 1.0   | 2500 | 0.2224          | 0.9275   | 0.9263 |
| 0.1877        | 2.0   | 5000 | 0.3141          | 0.9275   | 0.9274 |
| 0.1045        | 3.0   | 7500 | 0.3694          | 0.924    | 0.9242 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
