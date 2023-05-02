---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tweet_eval
metrics:
- f1
model-index:
- name: presentation_emotion_1234567
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: tweet_eval
      type: tweet_eval
      args: emotion
    metrics:
    - name: F1
      type: f1
      value: 0.7272977042723248
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# presentation_emotion_1234567

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the tweet_eval dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0237
- F1: 0.7273

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.18796906442746e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 1234567
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.1189        | 1.0   | 408  | 0.6827          | 0.7164 |
| 1.0678        | 2.0   | 816  | 0.6916          | 0.7396 |
| 0.6582        | 3.0   | 1224 | 0.9281          | 0.7276 |
| 0.0024        | 4.0   | 1632 | 1.0237          | 0.7273 |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.9.1
- Datasets 1.16.1
- Tokenizers 0.10.3
