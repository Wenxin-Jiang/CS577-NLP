---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: twitter_RoBERTa_token_itr0_1e-05_editorials_01_03_2022-15_00_35
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter_RoBERTa_token_itr0_1e-05_editorials_01_03_2022-15_00_35

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base](https://huggingface.co/cardiffnlp/twitter-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1155
- Precision: 0.5720
- Recall: 0.4705
- F1: 0.5163
- Accuracy: 0.9687

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
| No log        | 1.0   | 15   | 0.1256          | 0.04      | 0.0021 | 0.0039 | 0.9624   |
| No log        | 2.0   | 30   | 0.0963          | 0.7121    | 0.5711 | 0.6339 | 0.9794   |
| No log        | 3.0   | 45   | 0.0844          | 0.6205    | 0.5732 | 0.5959 | 0.9778   |
| No log        | 4.0   | 60   | 0.0770          | 0.6201    | 0.5856 | 0.6023 | 0.9778   |
| No log        | 5.0   | 75   | 0.0750          | 0.6174    | 0.5856 | 0.6011 | 0.9777   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
