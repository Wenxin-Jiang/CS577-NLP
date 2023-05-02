---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tweet_eval
metrics:
- f1
model-index:
- name: demo_emotion_1234567
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
      value: 0.7348035780583043
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# demo_emotion_1234567

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the tweet_eval dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9818
- F1: 0.7348

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.551070618629693e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 0
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| No log        | 1.0   | 204  | 0.7431          | 0.6530 |
| No log        | 2.0   | 408  | 0.6943          | 0.7333 |
| 0.5176        | 3.0   | 612  | 0.8456          | 0.7326 |
| 0.5176        | 4.0   | 816  | 0.9818          | 0.7348 |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.9.1
- Datasets 1.16.1
- Tokenizers 0.10.3
