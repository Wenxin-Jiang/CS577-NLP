---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tweet_eval
metrics:
- f1
model-index:
- name: sentiment_trained_31415
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: tweet_eval
      type: tweet_eval
      args: sentiment
    metrics:
    - name: F1
      type: f1
      value: 0.7188262432133108
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sentiment_trained_31415

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the tweet_eval dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2481
- F1: 0.7188

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1.2140338797769864e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 31415
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step  | Validation Loss | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 0.651         | 1.0   | 11404 | 0.6669          | 0.7141 |
| 0.6066        | 2.0   | 22808 | 0.8160          | 0.7198 |
| 0.503         | 3.0   | 34212 | 1.0659          | 0.7182 |
| 0.386         | 4.0   | 45616 | 1.2481          | 0.7188 |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.9.1
- Datasets 1.16.1
- Tokenizers 0.10.3
