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
      value: 0.9127878490935816
    - name: Recall
      type: recall
      value: 0.9405923931336251
    - name: F1
      type: f1
      value: 0.9264815582262743
    - name: Accuracy
      type: accuracy
      value: 0.9841937952551951
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0586
- Precision: 0.9128
- Recall: 0.9406
- F1: 0.9265
- Accuracy: 0.9842

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
- train_batch_size: 48
- eval_batch_size: 48
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 293  | 0.0844          | 0.8714    | 0.9123 | 0.8914 | 0.9760   |
| 0.1765        | 2.0   | 586  | 0.0601          | 0.9109    | 0.9357 | 0.9231 | 0.9834   |
| 0.1765        | 3.0   | 879  | 0.0586          | 0.9128    | 0.9406 | 0.9265 | 0.9842   |


### Framework versions

- Transformers 4.22.0
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
