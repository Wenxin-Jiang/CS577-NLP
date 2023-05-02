---
license: mit
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: my_ner_model1_2_split_by_sentence_
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# my_ner_model1_2_split_by_sentence_

This model is a fine-tuned version of [dbmdz/bert-base-turkish-cased](https://huggingface.co/dbmdz/bert-base-turkish-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2257
- Precision: 0.6377
- Recall: 0.7644
- F1: 0.6953
- Accuracy: 0.9401

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 427  | 0.2342          | 0.5265    | 0.6923 | 0.5981 | 0.9264   |
| 0.3433        | 2.0   | 854  | 0.1959          | 0.6024    | 0.7397 | 0.6640 | 0.9364   |
| 0.1686        | 3.0   | 1281 | 0.2085          | 0.6068    | 0.7608 | 0.6752 | 0.9376   |
| 0.1241        | 4.0   | 1708 | 0.2198          | 0.6376    | 0.7591 | 0.6931 | 0.9398   |
| 0.0912        | 5.0   | 2135 | 0.2257          | 0.6377    | 0.7644 | 0.6953 | 0.9401   |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu102
- Datasets 2.7.1
- Tokenizers 0.12.1
