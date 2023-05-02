---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: xlm-roberta-large-finetuned-combined-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-large-finetuned-combined-DS

This model is a fine-tuned version of [xlm-roberta-large](https://huggingface.co/xlm-roberta-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9169
- Accuracy: 0.6587
- Precision: 0.6417
- Recall: 0.6445
- F1: 0.6396

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
- train_batch_size: 8
- eval_batch_size: 16
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0116        | 0.5   | 711  | 0.9454          | 0.5892   | 0.6556    | 0.5190 | 0.4582 |
| 0.8678        | 1.0   | 1422 | 0.9676          | 0.6503   | 0.6383    | 0.6076 | 0.6103 |
| 0.7644        | 1.5   | 2133 | 0.8672          | 0.6355   | 0.6142    | 0.6206 | 0.6166 |
| 0.8198        | 2.0   | 2844 | 0.8319          | 0.6713   | 0.6460    | 0.6448 | 0.6453 |
| 0.6665        | 2.5   | 3555 | 0.8342          | 0.6538   | 0.6359    | 0.6414 | 0.6349 |
| 0.6473        | 3.0   | 4266 | 0.9169          | 0.6587   | 0.6417    | 0.6445 | 0.6396 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1
