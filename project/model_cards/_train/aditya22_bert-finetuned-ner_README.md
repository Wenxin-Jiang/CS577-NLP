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
      value: 0.936018564561578
    - name: Recall
      type: recall
      value: 0.9503534163581285
    - name: F1
      type: f1
      value: 0.9431315240083508
    - name: Accuracy
      type: accuracy
      value: 0.9859598516512628
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0642
- Precision: 0.9360
- Recall: 0.9504
- F1: 0.9431
- Accuracy: 0.9860

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
| 0.0855        | 1.0   | 1756 | 0.0642          | 0.9108    | 0.9387 | 0.9246 | 0.9834   |
| 0.0414        | 2.0   | 3512 | 0.0619          | 0.9331    | 0.9502 | 0.9415 | 0.9853   |
| 0.0181        | 3.0   | 5268 | 0.0642          | 0.9360    | 0.9504 | 0.9431 | 0.9860   |


### Framework versions

- Transformers 4.20.0
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
