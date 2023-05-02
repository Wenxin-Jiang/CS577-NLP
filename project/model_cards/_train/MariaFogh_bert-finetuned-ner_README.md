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
      config: en
      split: train
      args: en
    metrics:
    - name: Precision
      type: precision
      value: 0.8168753849312256
    - name: Recall
      type: recall
      value: 0.8438427824119893
    - name: F1
      type: f1
      value: 0.8301401300462463
    - name: Accuracy
      type: accuracy
      value: 0.9274749936443093
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the wikiann dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3141
- Precision: 0.8169
- Recall: 0.8438
- F1: 0.8301
- Accuracy: 0.9275

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
| 0.285         | 1.0   | 2500 | 0.2839          | 0.8005    | 0.8224 | 0.8113 | 0.9201   |
| 0.2052        | 2.0   | 5000 | 0.2599          | 0.8028    | 0.8383 | 0.8202 | 0.9254   |
| 0.1419        | 3.0   | 7500 | 0.3141          | 0.8169    | 0.8438 | 0.8301 | 0.9275   |


### Framework versions

- Transformers 4.23.0
- Pytorch 1.12.1+cu113
- Datasets 2.5.2
- Tokenizers 0.13.1
