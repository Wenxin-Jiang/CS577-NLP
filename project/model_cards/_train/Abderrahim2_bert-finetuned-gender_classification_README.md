---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
- accuracy
model-index:
- name: bert-finetuned-gender_classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-gender_classification

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1484
- F1: 0.9645
- Roc Auc: 0.9732
- Accuracy: 0.964

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | F1     | Roc Auc | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:-------:|:--------:|
| 0.1679        | 1.0   | 1125  | 0.1781          | 0.928  | 0.946   | 0.927    |
| 0.1238        | 2.0   | 2250  | 0.1252          | 0.9516 | 0.9640  | 0.95     |
| 0.0863        | 3.0   | 3375  | 0.1283          | 0.9515 | 0.9637  | 0.95     |
| 0.0476        | 4.0   | 4500  | 0.1419          | 0.9565 | 0.9672  | 0.956    |
| 0.0286        | 5.0   | 5625  | 0.1428          | 0.9555 | 0.9667  | 0.954    |
| 0.0091        | 6.0   | 6750  | 0.1515          | 0.9604 | 0.9700  | 0.959    |
| 0.0157        | 7.0   | 7875  | 0.1535          | 0.9580 | 0.9682  | 0.957    |
| 0.0048        | 8.0   | 9000  | 0.1484          | 0.9645 | 0.9732  | 0.964    |
| 0.0045        | 9.0   | 10125 | 0.1769          | 0.9605 | 0.9703  | 0.96     |
| 0.0037        | 10.0  | 11250 | 0.2007          | 0.9565 | 0.9672  | 0.956    |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
