---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- conll2003
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-cased-ner-fcit499
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      config: conll2003
      split: train
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9417409184372858
    - name: Recall
      type: recall
      value: 0.950207468879668
    - name: F1
      type: f1
      value: 0.9459552495697073
    - name: Accuracy
      type: accuracy
      value: 0.9905416329830234
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-cased-ner-fcit499

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0404
- Precision: 0.9417
- Recall: 0.9502
- F1: 0.9460
- Accuracy: 0.9905

## Model description

More information neededx

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 157  | 0.0578          | 0.8782    | 0.8976 | 0.8878 | 0.9825   |
| No log        | 2.0   | 314  | 0.0425          | 0.9317    | 0.9343 | 0.9330 | 0.9885   |
| No log        | 3.0   | 471  | 0.0391          | 0.9381    | 0.9433 | 0.9407 | 0.9897   |
| 0.1097        | 4.0   | 628  | 0.0397          | 0.9377    | 0.9467 | 0.9422 | 0.9900   |
| 0.1097        | 5.0   | 785  | 0.0404          | 0.9417    | 0.9502 | 0.9460 | 0.9905   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.2
