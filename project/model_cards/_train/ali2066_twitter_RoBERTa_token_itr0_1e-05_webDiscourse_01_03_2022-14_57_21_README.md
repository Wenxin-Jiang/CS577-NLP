---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: twitter_RoBERTa_token_itr0_1e-05_webDiscourse_01_03_2022-14_57_21
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter_RoBERTa_token_itr0_1e-05_webDiscourse_01_03_2022-14_57_21

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base](https://huggingface.co/cardiffnlp/twitter-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5905
- Precision: 0.0024
- Recall: 0.0143
- F1: 0.0041
- Accuracy: 0.6867

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
| No log        | 1.0   | 10   | 0.6081          | 0.0       | 0.0    | 0.0    | 0.6904   |
| No log        | 2.0   | 20   | 0.6014          | 0.0025    | 0.0130 | 0.0042 | 0.6934   |
| No log        | 3.0   | 30   | 0.5953          | 0.0       | 0.0    | 0.0    | 0.6930   |
| No log        | 4.0   | 40   | 0.5858          | 0.0       | 0.0    | 0.0    | 0.6941   |
| No log        | 5.0   | 50   | 0.5815          | 0.0       | 0.0    | 0.0    | 0.6947   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
