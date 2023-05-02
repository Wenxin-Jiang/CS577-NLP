---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imdb
metrics:
- accuracy
model-index:
- name: bert-finetuned-imdb
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: imdb
      type: imdb
      args: plain_text
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.866
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-imdb

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the imdb dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5591
- Accuracy: 0.866

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 125  | 0.4995          | 0.79     |
| No log        | 2.0   | 250  | 0.4000          | 0.854    |
| No log        | 3.0   | 375  | 0.5591          | 0.866    |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
