---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tweet_eval
metrics:
- f1
model-index:
- name: demo_sentiment_31415
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
      value: 0.7113620044371958
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# demo_sentiment_31415

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the tweet_eval dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6332
- F1: 0.7114

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 8.62486660723695e-06
- train_batch_size: 64
- eval_batch_size: 64
- seed: 0
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.7592        | 1.0   | 713  | 0.6509          | 0.6834 |
| 0.6389        | 2.0   | 1426 | 0.6318          | 0.7011 |
| 0.5647        | 3.0   | 2139 | 0.6320          | 0.7041 |
| 0.5391        | 4.0   | 2852 | 0.6332          | 0.7114 |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.9.1
- Datasets 1.16.1
- Tokenizers 0.10.3
