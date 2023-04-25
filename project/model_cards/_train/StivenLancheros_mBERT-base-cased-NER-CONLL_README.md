---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- conll2002
- conll2003
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: mBERT-base-cased-NER-CONLL
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2002
      type: conll2002
      args: es
    metrics:
    - name: Precision
      type: precision
      value: 0.8621083924079579
    - name: Recall
      type: recall
      value: 0.8662683823529411
    - name: F1
      type: f1
      value: 0.8641833810888252
    - name: Accuracy
      type: accuracy
      value: 0.9790639230580277
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mBERT-base-cased-NER-CONLL (EN-ES)

This model is a fine-tuned version of [bert-base-multilingual-cased ](https://huggingface.co/bert-base-multilingual-cased) on the conll2003 and conll2002 datasets. Training was performed separately.
It achieves the following results on the evaluation set:

Connll2003:
- Loss: 0.0585
- Precision: 0.9489
- Recall: 0.9541
- F1: 0.9515
- Accuracy: 0.9880

Conll2002:
- Loss: 0.1435
- Precision: 0.8621
- Recall: 0.8663
- F1: 0.8642
- Accuracy: 0.9791

## Model description

IOB tagging Scheme. PER/LOC/MISC/ORG tags

## Intended uses & limitations

More information needed

## Training and evaluation data

Conll2002/2003 (ES-EN)

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

Conll2003:

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1739        | 1.0   | 878  | 0.0741          | 0.9246    | 0.9181 | 0.9213 | 0.9823   |
| 0.045         | 2.0   | 1756 | 0.0586          | 0.9469    | 0.9476 | 0.9472 | 0.9870   |
| 0.0213        | 3.0   | 2634 | 0.0583          | 0.9503    | 0.9510 | 0.9506 | 0.9877   |
| 0.0113        | 4.0   | 3512 | 0.0585          | 0.9489    | 0.9541 | 0.9515 | 0.9880   |


Conll2002:

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0739        | 1.0   | 4162  | 0.1322          | 0.8430    | 0.8267 | 0.8348 | 0.9741   |
| 0.0454        | 2.0   | 8324  | 0.1158          | 0.8664    | 0.8614 | 0.8639 | 0.9782   |
| 0.031         | 3.0   | 12486 | 0.1243          | 0.8521    | 0.8660 | 0.8590 | 0.9783   |
| 0.0136        | 4.0   | 16648 | 0.1435          | 0.8621    | 0.8663 | 0.8642 | 0.9791   |


### Framework versions

- Transformers 4.12.3
- Pytorch 1.10.0+cu111
- Datasets 1.15.1
- Tokenizers 0.10.3
