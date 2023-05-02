---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: twitter-data-distilbert-base-uncased-sentiment-finetuned-memes-test
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter-data-distilbert-base-uncased-sentiment-finetuned-memes-test

This model is a fine-tuned version of [jayantapaul888/twitter-data-distilbert-base-uncased-sentiment-finetuned-memes](https://huggingface.co/jayantapaul888/twitter-data-distilbert-base-uncased-sentiment-finetuned-memes) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6985
- Accuracy: 0.8218
- Precision: 0.8225
- Recall: 0.8218
- F1: 0.8221

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
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 1.0   | 294  | 0.4189          | 0.8124   | 0.8151    | 0.8124 | 0.8136 |
| 0.4351        | 2.0   | 588  | 0.4057          | 0.8258   | 0.8275    | 0.8258 | 0.8263 |
| 0.4351        | 3.0   | 882  | 0.4628          | 0.8220   | 0.8244    | 0.8220 | 0.8224 |
| 0.2248        | 4.0   | 1176 | 0.5336          | 0.8250   | 0.8258    | 0.8250 | 0.8253 |
| 0.2248        | 5.0   | 1470 | 0.6466          | 0.8208   | 0.8217    | 0.8208 | 0.8212 |
| 0.1158        | 6.0   | 1764 | 0.6985          | 0.8218   | 0.8225    | 0.8218 | 0.8221 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
