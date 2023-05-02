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
- name: distilbert-sentiment-new
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-sentiment-new

This model is a fine-tuned version of [distilbert-base-multilingual-cased](https://huggingface.co/distilbert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5872
- Accuracy: 0.7243
- Precision: 0.7192
- Recall: 0.7243
- F1: 0.7175

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 1.0   | 296  | 0.6038          | 0.6787   | 0.7049    | 0.6787 | 0.6235 |
| 0.5926        | 2.0   | 592  | 0.5532          | 0.7148   | 0.7118    | 0.7148 | 0.6994 |
| 0.5926        | 3.0   | 888  | 0.5480          | 0.7243   | 0.7199    | 0.7243 | 0.7144 |
| 0.4946        | 4.0   | 1184 | 0.5535          | 0.7300   | 0.7255    | 0.7300 | 0.7220 |
| 0.4946        | 5.0   | 1480 | 0.5858          | 0.7186   | 0.7140    | 0.7186 | 0.7146 |
| 0.4267        | 6.0   | 1776 | 0.5872          | 0.7243   | 0.7192    | 0.7243 | 0.7175 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
