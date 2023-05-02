---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: twitter-roberta-base-sentiment_token_itr0_2e-05_all_01_03_2022-04_19_45
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter-roberta-base-sentiment_token_itr0_2e-05_all_01_03_2022-04_19_45

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base-sentiment](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2858
- Precision: 0.3206
- Recall: 0.4721
- F1: 0.3819
- Accuracy: 0.8762

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
| No log        | 1.0   | 30   | 0.3772          | 0.0269    | 0.0326 | 0.0294 | 0.8143   |
| No log        | 2.0   | 60   | 0.3052          | 0.2015    | 0.3596 | 0.2583 | 0.8537   |
| No log        | 3.0   | 90   | 0.2937          | 0.2737    | 0.4273 | 0.3337 | 0.8722   |
| No log        | 4.0   | 120  | 0.2852          | 0.2728    | 0.4348 | 0.3353 | 0.8750   |
| No log        | 5.0   | 150  | 0.2676          | 0.2851    | 0.4474 | 0.3483 | 0.8797   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
