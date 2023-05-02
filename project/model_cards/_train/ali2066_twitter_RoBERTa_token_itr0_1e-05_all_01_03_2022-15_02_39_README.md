---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: twitter_RoBERTa_token_itr0_1e-05_all_01_03_2022-15_02_39
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter_RoBERTa_token_itr0_1e-05_all_01_03_2022-15_02_39

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base](https://huggingface.co/cardiffnlp/twitter-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2903
- Precision: 0.2440
- Recall: 0.4465
- F1: 0.3155
- Accuracy: 0.8706

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 30   | 0.4378          | 0.0463    | 0.1136 | 0.0658 | 0.7742   |
| No log        | 2.0   | 60   | 0.3739          | 0.1472    | 0.3756 | 0.2115 | 0.8284   |
| No log        | 3.0   | 90   | 0.3422          | 0.1865    | 0.4330 | 0.2607 | 0.8374   |
| No log        | 4.0   | 120  | 0.3286          | 0.2243    | 0.4833 | 0.3064 | 0.8438   |
| No log        | 5.0   | 150  | 0.3239          | 0.2356    | 0.4809 | 0.3163 | 0.8490   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
