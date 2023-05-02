---
tags:
- generated_from_trainer
model-index:
- name: GPT2-CLS-Finetuned-MBTI
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# GPT2-CLS-Finetuned-MBTI

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9571
- Cls loss: 1.9559
- Cls Accuracy: 0.6052
- Cls F1: 0.5956
- Cls Precision: 0.6180
- Cls Recall: 0.6052

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Cls loss | Cls Accuracy | Cls F1 | Cls Precision | Cls Recall | Validation Loss |
|:-------------:|:-----:|:-----:|:--------:|:------------:|:------:|:-------------:|:----------:|:---------------:|
| 2.0239        | 1.0   | 3470  | 1.7000   | 0.5262       | 0.4961 | 0.5438        | 0.5262     | 1.6998          |
| 1.5182        | 2.0   | 6940  | 1.8171   | 0.5873       | 0.5764 | 0.5971        | 0.5873     | 1.8181          |
| 1.3241        | 3.0   | 10410 | 1.9559   | 0.6052       | 0.5956 | 0.6180        | 0.6052     | 1.9571          |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
