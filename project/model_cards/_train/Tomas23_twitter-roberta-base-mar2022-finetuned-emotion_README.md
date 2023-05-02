---
tags:
- generated_from_trainer
datasets:
- tweet_eval
metrics:
- accuracy
- f1
model-index:
- name: twitter-roberta-base-mar2022-finetuned-emotion
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: tweet_eval
      type: tweet_eval
      args: emotion
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8191414496833216
    - name: F1
      type: f1
      value: 0.8170974933422602
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter-roberta-base-mar2022-finetuned-emotion

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base-mar2022](https://huggingface.co/cardiffnlp/twitter-roberta-base-mar2022) on the tweet_eval dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5146
- Accuracy: 0.8191
- F1: 0.8171

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.8945        | 1.0   | 102  | 0.5831          | 0.7995   | 0.7887 |
| 0.5176        | 2.0   | 204  | 0.5266          | 0.8235   | 0.8200 |


### Framework versions

- Transformers 4.19.3
- Pytorch 1.11.0+cu102
- Datasets 2.2.2
- Tokenizers 0.12.1
