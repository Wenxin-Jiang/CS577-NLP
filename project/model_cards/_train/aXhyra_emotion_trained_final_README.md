---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tweet_eval
metrics:
- f1
model-index:
- name: emotion_trained_final
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
      value: 0.7469065445487402
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# emotion_trained_final

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the tweet_eval dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9349
- F1: 0.7469

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1.502523631581398e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 0
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.9013        | 1.0   | 815  | 0.7822          | 0.6470 |
| 0.5008        | 2.0   | 1630 | 0.7142          | 0.7419 |
| 0.3684        | 3.0   | 2445 | 0.8621          | 0.7443 |
| 0.2182        | 4.0   | 3260 | 0.9349          | 0.7469 |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.9.1
- Datasets 1.16.1
- Tokenizers 0.10.3
