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
      value: 0.9317394888705688
    - name: Recall
      type: recall
      value: 0.9510265903736116
    - name: F1
      type: f1
      value: 0.9412842508536686
    - name: Accuracy
      type: accuracy
      value: 0.9865779713898863
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0603
- Precision: 0.9317
- Recall: 0.9510
- F1: 0.9413
- Accuracy: 0.9866

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
| 0.0872        | 1.0   | 1756 | 0.0660          | 0.9152    | 0.9350 | 0.9250 | 0.9827   |
| 0.0386        | 2.0   | 3512 | 0.0579          | 0.9374    | 0.9498 | 0.9436 | 0.9864   |
| 0.0225        | 3.0   | 5268 | 0.0603          | 0.9317    | 0.9510 | 0.9413 | 0.9866   |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.10.0+cu111
- Datasets 1.16.1
- Tokenizers 0.10.3
