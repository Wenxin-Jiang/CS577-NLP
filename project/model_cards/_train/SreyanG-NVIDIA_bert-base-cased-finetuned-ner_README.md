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
- name: bert-base-cased-finetuned-ner
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
      value: 0.9325301204819277
    - name: Recall
      type: recall
      value: 0.9374663556432801
    - name: F1
      type: f1
      value: 0.9349917229654156
    - name: Accuracy
      type: accuracy
      value: 0.9840466238888562
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-cased-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0650
- Precision: 0.9325
- Recall: 0.9375
- F1: 0.9350
- Accuracy: 0.9840

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.2346        | 1.0   | 878  | 0.0722          | 0.9168    | 0.9217 | 0.9192 | 0.9795   |
| 0.0483        | 2.0   | 1756 | 0.0618          | 0.9299    | 0.9370 | 0.9335 | 0.9837   |
| 0.0262        | 3.0   | 2634 | 0.0650          | 0.9325    | 0.9375 | 0.9350 | 0.9840   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu102
- Datasets 2.1.0
- Tokenizers 0.12.1
