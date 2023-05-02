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
- name: xlm-roberta-base-finetuned-code-mixed-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-finetuned-code-mixed-DS

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8266
- Accuracy: 0.6318
- Precision: 0.5781
- Recall: 0.5978
- F1: 0.5677

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4.932923543227153e-05
- train_batch_size: 16
- eval_batch_size: 32
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0602        | 1.0   | 248  | 1.0280          | 0.5211   | 0.4095    | 0.4557 | 0.3912 |
| 0.9741        | 1.99  | 496  | 0.9318          | 0.5533   | 0.4758    | 0.5002 | 0.4415 |
| 0.8585        | 2.99  | 744  | 0.8585          | 0.6076   | 0.5539    | 0.5731 | 0.5353 |
| 0.7293        | 3.98  | 992  | 0.8266          | 0.6318   | 0.5781    | 0.5978 | 0.5677 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1
