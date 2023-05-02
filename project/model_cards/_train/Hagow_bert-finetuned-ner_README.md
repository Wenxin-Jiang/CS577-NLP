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
      config: conll2003
      split: train
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.937251655629139
    - name: Recall
      type: recall
      value: 0.9527095254123191
    - name: F1
      type: f1
      value: 0.9449173760640961
    - name: Accuracy
      type: accuracy
      value: 0.9866515570730559
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0620
- Precision: 0.9373
- Recall: 0.9527
- F1: 0.9449
- Accuracy: 0.9867

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
| 0.0848        | 1.0   | 1756 | 0.0639          | 0.9093    | 0.9362 | 0.9226 | 0.9834   |
| 0.0347        | 2.0   | 3512 | 0.0638          | 0.9265    | 0.9488 | 0.9376 | 0.9857   |
| 0.0178        | 3.0   | 5268 | 0.0620          | 0.9373    | 0.9527 | 0.9449 | 0.9867   |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
