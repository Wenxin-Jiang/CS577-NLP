---
license: mit
tags:
- generated_from_trainer
metrics:
- f1
- accuracy
model-index:
- name: bert-finetuned-Location
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-Location

This model is a fine-tuned version of [dbmdz/bert-base-french-europeana-cased](https://huggingface.co/dbmdz/bert-base-french-europeana-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5462
- F1: 0.8167
- Roc Auc: 0.8624
- Accuracy: 0.8133

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
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     | Roc Auc | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:------:|:-------:|:--------:|
| 0.4229        | 1.0   | 742  | 0.3615          | 0.7402 | 0.8014  | 0.6900   |
| 0.3722        | 2.0   | 1484 | 0.3103          | 0.7906 | 0.8416  | 0.7796   |
| 0.262         | 3.0   | 2226 | 0.3364          | 0.8135 | 0.8600  | 0.8100   |
| 0.2239        | 4.0   | 2968 | 0.4593          | 0.8085 | 0.8561  | 0.8066   |
| 0.1461        | 5.0   | 3710 | 0.5534          | 0.7923 | 0.8440  | 0.7904   |
| 0.1333        | 6.0   | 4452 | 0.5462          | 0.8167 | 0.8624  | 0.8133   |
| 0.0667        | 7.0   | 5194 | 0.6298          | 0.7972 | 0.8479  | 0.7958   |
| 0.0616        | 8.0   | 5936 | 0.6362          | 0.8075 | 0.8556  | 0.8059   |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
