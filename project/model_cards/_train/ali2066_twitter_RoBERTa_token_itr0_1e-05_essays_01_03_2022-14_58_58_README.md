---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: twitter_RoBERTa_token_itr0_1e-05_essays_01_03_2022-14_58_58
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter_RoBERTa_token_itr0_1e-05_essays_01_03_2022-14_58_58

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base](https://huggingface.co/cardiffnlp/twitter-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2698
- Precision: 0.3554
- Recall: 0.4884
- F1: 0.4114
- Accuracy: 0.8973

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
| No log        | 1.0   | 11   | 0.4423          | 0.0261    | 0.0184 | 0.0216 | 0.7728   |
| No log        | 2.0   | 22   | 0.3220          | 0.1256    | 0.3129 | 0.1793 | 0.8735   |
| No log        | 3.0   | 33   | 0.2561          | 0.2633    | 0.4264 | 0.3255 | 0.9103   |
| No log        | 4.0   | 44   | 0.2535          | 0.3303    | 0.4509 | 0.3813 | 0.9115   |
| No log        | 5.0   | 55   | 0.2414          | 0.3696    | 0.4693 | 0.4135 | 0.9181   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
