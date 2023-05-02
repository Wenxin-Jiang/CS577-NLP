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
- name: bert-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9354518371400199
    - name: Recall
      type: recall
      value: 0.9511948838774823
    - name: F1
      type: f1
      value: 0.9432576769025368
    - name: Accuracy
      type: accuracy
      value: 0.9868870312591982
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0598
- Precision: 0.9355
- Recall: 0.9512
- F1: 0.9433
- Accuracy: 0.9869

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

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0833        | 1.0   | 1756 | 0.0654          | 0.9202    | 0.9350 | 0.9275 | 0.9833   |
| 0.034         | 2.0   | 3512 | 0.0610          | 0.9262    | 0.9458 | 0.9359 | 0.9846   |
| 0.0233        | 3.0   | 5268 | 0.0598          | 0.9355    | 0.9512 | 0.9433 | 0.9869   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.1.0
- Tokenizers 0.12.1
