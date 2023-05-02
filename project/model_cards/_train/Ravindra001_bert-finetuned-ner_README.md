---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wikiann
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
      name: wikiann
      type: wikiann
      args: en
    metrics:
    - name: Precision
      type: precision
      value: 0.819622641509434
    - name: Recall
      type: recall
      value: 0.8444790046656299
    - name: F1
      type: f1
      value: 0.8318651857525853
    - name: Accuracy
      type: accuracy
      value: 0.9269227060339613
  - task:
      type: token-classification
      name: Token Classification
    dataset:
      name: wikiann
      type: wikiann
      config: en
      split: test
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8492771401033908
      verified: true
    - name: Precision
      type: precision
      value: 0.857294905524994
      verified: true
    - name: Recall
      type: recall
      value: 0.865900059186607
      verified: true
    - name: F1
      type: f1
      value: 0.8615759964905745
      verified: true
    - name: loss
      type: loss
      value: 1.054654836654663
      verified: true
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the wikiann dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3217
- Precision: 0.8196
- Recall: 0.8445
- F1: 0.8319
- Accuracy: 0.9269

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
| 0.2821        | 1.0   | 2500 | 0.2906          | 0.7983    | 0.8227 | 0.8103 | 0.9193   |
| 0.2087        | 2.0   | 5000 | 0.2614          | 0.8030    | 0.8379 | 0.8201 | 0.9257   |
| 0.1404        | 3.0   | 7500 | 0.3217          | 0.8196    | 0.8445 | 0.8319 | 0.9269   |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
