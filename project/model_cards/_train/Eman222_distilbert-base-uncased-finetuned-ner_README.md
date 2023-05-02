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
- name: distilbert-base-uncased-finetuned-ner
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
      value: 0.9261759822910902
    - name: Recall
      type: recall
      value: 0.9361226087929299
    - name: F1
      type: f1
      value: 0.9311227328363192
    - name: Accuracy
      type: accuracy
      value: 0.9837164598789457
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0611
- Precision: 0.9262
- Recall: 0.9361
- F1: 0.9311
- Accuracy: 0.9837

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
| 0.2401        | 1.0   | 878  | 0.0684          | 0.9147    | 0.9172 | 0.9159 | 0.9808   |
| 0.0538        | 2.0   | 1756 | 0.0614          | 0.9231    | 0.9346 | 0.9288 | 0.9829   |
| 0.0301        | 3.0   | 2634 | 0.0611          | 0.9262    | 0.9361 | 0.9311 | 0.9837   |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
