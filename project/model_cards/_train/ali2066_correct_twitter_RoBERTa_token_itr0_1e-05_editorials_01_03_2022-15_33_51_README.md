---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: correct_twitter_RoBERTa_token_itr0_1e-05_editorials_01_03_2022-15_33_51
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# correct_twitter_RoBERTa_token_itr0_1e-05_editorials_01_03_2022-15_33_51

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base](https://huggingface.co/cardiffnlp/twitter-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1138
- Precision: 0.5788
- Recall: 0.4712
- F1: 0.5195
- Accuracy: 0.9688

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
| No log        | 1.0   | 15   | 0.1316          | 0.04      | 0.0021 | 0.0040 | 0.9624   |
| No log        | 2.0   | 30   | 0.1016          | 0.6466    | 0.4688 | 0.5435 | 0.9767   |
| No log        | 3.0   | 45   | 0.0899          | 0.5873    | 0.4625 | 0.5175 | 0.9757   |
| No log        | 4.0   | 60   | 0.0849          | 0.5984    | 0.4813 | 0.5335 | 0.9761   |
| No log        | 5.0   | 75   | 0.0835          | 0.5984    | 0.4813 | 0.5335 | 0.9761   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
