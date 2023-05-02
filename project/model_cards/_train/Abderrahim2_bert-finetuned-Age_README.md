---
license: mit
tags:
- generated_from_trainer
metrics:
- f1
- accuracy
model-index:
- name: bert-finetuned-Age
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-Age

This model is a fine-tuned version of [dbmdz/bert-base-french-europeana-cased](https://huggingface.co/dbmdz/bert-base-french-europeana-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4642
- F1: 0.7254
- Roc Auc: 0.7940
- Accuracy: 0.7249

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
| 0.4564        | 1.0   | 965  | 0.4642          | 0.7254 | 0.7940  | 0.7254   |
| 0.4443        | 2.0   | 1930 | 0.4662          | 0.7254 | 0.7940  | 0.7254   |
| 0.4388        | 3.0   | 2895 | 0.4628          | 0.7254 | 0.7940  | 0.7254   |
| 0.4486        | 4.0   | 3860 | 0.4642          | 0.7254 | 0.7940  | 0.7249   |
| 0.4287        | 5.0   | 4825 | 0.4958          | 0.7214 | 0.7907  | 0.7150   |
| 0.4055        | 6.0   | 5790 | 0.5325          | 0.6961 | 0.7715  | 0.6782   |
| 0.3514        | 7.0   | 6755 | 0.5588          | 0.6586 | 0.7443  | 0.6223   |
| 0.3227        | 8.0   | 7720 | 0.5944          | 0.6625 | 0.7470  | 0.6295   |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
