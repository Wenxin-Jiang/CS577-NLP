---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: finetuned_token_2e-05_all_16_02_2022-16_06_20
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_2e-05_all_16_02_2022-16_06_20

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1750
- Precision: 0.3286
- Recall: 0.3334
- F1: 0.3310
- Accuracy: 0.9447

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 38   | 0.3355          | 0.0975    | 0.2358 | 0.1380 | 0.8361   |
| No log        | 2.0   | 76   | 0.3177          | 0.1359    | 0.2709 | 0.1810 | 0.8398   |
| No log        | 3.0   | 114  | 0.3000          | 0.1542    | 0.3043 | 0.2047 | 0.8471   |
| No log        | 4.0   | 152  | 0.3033          | 0.1589    | 0.3060 | 0.2091 | 0.8434   |
| No log        | 5.0   | 190  | 0.3029          | 0.1629    | 0.3110 | 0.2138 | 0.8447   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
