---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tweet_eval
metrics:
- precision
- recall
model-index:
- name: bert-emotion
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: tweet_eval
      type: tweet_eval
      config: emotion
      split: train
      args: emotion
    metrics:
    - name: Precision
      type: precision
      value: 0.7071669427034283
    - name: Recall
      type: recall
      value: 0.723286061789479
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-emotion

This model is a fine-tuned version of [distilbert-base-cased](https://huggingface.co/distilbert-base-cased) on the tweet_eval dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2053
- Precision: 0.7072
- Recall: 0.7233
- Fscore: 0.7124

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | Fscore |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|
| 0.8623        | 1.0   | 815  | 0.7198          | 0.7536    | 0.6312 | 0.6559 |
| 0.5637        | 2.0   | 1630 | 0.8756          | 0.7213    | 0.7166 | 0.7160 |
| 0.2845        | 3.0   | 2445 | 1.2053          | 0.7072    | 0.7233 | 0.7124 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
