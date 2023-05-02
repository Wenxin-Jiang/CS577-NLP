---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: correct_twitter_RoBERTa_token_itr0_1e-05_essays_01_03_2022-15_32_16
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# correct_twitter_RoBERTa_token_itr0_1e-05_essays_01_03_2022-15_32_16

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base](https://huggingface.co/cardiffnlp/twitter-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2663
- Precision: 0.3644
- Recall: 0.4985
- F1: 0.4210
- Accuracy: 0.8997

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
| No log        | 1.0   | 11   | 0.5174          | 0.0120    | 0.0061 | 0.0081 | 0.6997   |
| No log        | 2.0   | 22   | 0.4029          | 0.1145    | 0.3098 | 0.1672 | 0.8265   |
| No log        | 3.0   | 33   | 0.3604          | 0.2539    | 0.4448 | 0.3233 | 0.8632   |
| No log        | 4.0   | 44   | 0.3449          | 0.2992    | 0.4755 | 0.3673 | 0.8704   |
| No log        | 5.0   | 55   | 0.3403          | 0.3340    | 0.4816 | 0.3945 | 0.8760   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
