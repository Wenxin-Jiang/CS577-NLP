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
- name: twitter-data-bert-base-multilingual-uncased-hindi-only-memes
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter-data-bert-base-multilingual-uncased-hindi-only-memes

This model is a fine-tuned version of [bert-base-multilingual-uncased](https://huggingface.co/bert-base-multilingual-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5614
- Accuracy: 0.9031
- Precision: 0.9064
- Recall: 0.9057
- F1: 0.9060

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.5408        | 1.0   | 511  | 0.4798          | 0.7974   | 0.8447    | 0.8049 | 0.7940 |
| 0.3117        | 2.0   | 1022 | 0.3576          | 0.8844   | 0.8875    | 0.8882 | 0.8869 |
| 0.2019        | 3.0   | 1533 | 0.3401          | 0.9020   | 0.9076    | 0.9047 | 0.9052 |
| 0.1364        | 4.0   | 2044 | 0.4519          | 0.8888   | 0.8936    | 0.8921 | 0.8923 |
| 0.0767        | 5.0   | 2555 | 0.5251          | 0.8987   | 0.9024    | 0.9016 | 0.9019 |
| 0.0433        | 6.0   | 3066 | 0.5614          | 0.9031   | 0.9064    | 0.9057 | 0.9060 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
