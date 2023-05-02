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
- name: xlm-roberta-large-finetuned-TRAC-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-large-finetuned-TRAC-DS

This model is a fine-tuned version of [xlm-roberta-large](https://huggingface.co/xlm-roberta-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0992
- Accuracy: 0.3342
- Precision: 0.1114
- Recall: 0.3333
- F1: 0.1670

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4.1187640010910775e-05
- train_batch_size: 4
- eval_batch_size: 8
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.1358        | 0.25  | 612  | 1.1003          | 0.4436   | 0.1479    | 0.3333 | 0.2049 |
| 1.1199        | 0.5   | 1224 | 1.1130          | 0.4436   | 0.1479    | 0.3333 | 0.2049 |
| 1.1221        | 0.75  | 1836 | 1.0992          | 0.3342   | 0.1114    | 0.3333 | 0.1670 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1
