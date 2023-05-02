---
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: twitter_RoBERTa_base_sentence_itr0_1e-05_all_01_03_2022-13_53_11
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter_RoBERTa_base_sentence_itr0_1e-05_all_01_03_2022-13_53_11

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base](https://huggingface.co/cardiffnlp/twitter-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4118
- Accuracy: 0.8446
- F1: 0.8968
- Precision: 0.8740
- Recall: 0.9207

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| No log        | 1.0   | 390  | 0.3532          | 0.8451   | 0.8990 | 0.8997    | 0.8983 |
| 0.4111        | 2.0   | 780  | 0.3381          | 0.8561   | 0.9080 | 0.8913    | 0.9253 |
| 0.3031        | 3.0   | 1170 | 0.3490          | 0.8537   | 0.9034 | 0.9152    | 0.8919 |
| 0.2408        | 4.0   | 1560 | 0.3562          | 0.8671   | 0.9148 | 0.9       | 0.9300 |
| 0.2408        | 5.0   | 1950 | 0.3725          | 0.8659   | 0.9131 | 0.9074    | 0.9189 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
