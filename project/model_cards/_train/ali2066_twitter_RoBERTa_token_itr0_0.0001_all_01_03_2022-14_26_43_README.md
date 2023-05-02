---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: twitter_RoBERTa_token_itr0_0.0001_all_01_03_2022-14_26_43
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter_RoBERTa_token_itr0_0.0001_all_01_03_2022-14_26_43

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base](https://huggingface.co/cardiffnlp/twitter-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2591
- Precision: 0.4174
- Recall: 0.5678
- F1: 0.4811
- Accuracy: 0.8852

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 30   | 0.4690          | 0.3732    | 0.1830 | 0.2456 | 0.7509   |
| No log        | 2.0   | 60   | 0.3936          | 0.2067    | 0.3559 | 0.2615 | 0.7851   |
| No log        | 3.0   | 90   | 0.3019          | 0.3658    | 0.4904 | 0.4190 | 0.8703   |
| No log        | 4.0   | 120  | 0.2510          | 0.4387    | 0.5137 | 0.4732 | 0.8889   |
| No log        | 5.0   | 150  | 0.2481          | 0.4196    | 0.5511 | 0.4764 | 0.8881   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
