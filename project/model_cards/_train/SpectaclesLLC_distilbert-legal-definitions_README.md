---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: distilbert-legal-definitions
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-legal-definitions

This model is a fine-tuned version of [distilbert-base-cased](https://huggingface.co/distilbert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0034
- Precision: 0.9668
- Recall: 0.9707
- Macro F1: 0.9688
- Micro F1: 0.9688
- Accuracy: 0.9994
- Term F1: 0.9688
- Term Precision: 0.9668
- Term Recall: 0.9707

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | Macro F1 | Micro F1 | Accuracy | Term F1 | Term Precision | Term Recall |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:--------:|:--------:|:--------:|:-------:|:--------------:|:-----------:|
| 0.0049        | 1.0   | 2325 | 0.0034          | 0.9790    | 0.9580 | 0.9684   | 0.9684   | 0.9993   | 0.9684  | 0.9790         | 0.9580      |
| 0.0023        | 2.0   | 4650 | 0.0032          | 0.9669    | 0.9786 | 0.9727   | 0.9727   | 0.9994   | 0.9727  | 0.9669         | 0.9786      |
| 0.0013        | 3.0   | 6975 | 0.0018          | 0.9836    | 0.9794 | 0.9815   | 0.9815   | 0.9997   | 0.9815  | 0.9836         | 0.9794      |
| 0.0006        | 4.0   | 9300 | 0.0016          | 0.9879    | 0.9828 | 0.9854   | 0.9854   | 0.9997   | 0.9854  | 0.9879         | 0.9828      |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
