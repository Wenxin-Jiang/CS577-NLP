---
tags:
- generated_from_trainer
metrics:
- f1
- accuracy
model-index:
- name: xlm-roberta-base
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1437
- F1: 0.6011
- Roc Auc: 0.7429
- Accuracy: 0.4893

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     | Roc Auc | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:------:|:-------:|:--------:|
| 0.1911        | 1.0   | 1336 | 0.1682          | 0.5027 | 0.6816  | 0.3685   |
| 0.1506        | 2.0   | 2672 | 0.1485          | 0.5670 | 0.7204  | 0.4489   |
| 0.1379        | 3.0   | 4008 | 0.1437          | 0.6011 | 0.7429  | 0.4893   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
