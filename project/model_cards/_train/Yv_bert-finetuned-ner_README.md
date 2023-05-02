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
      value: 0.9369817578772802
    - name: Recall
      type: recall
      value: 0.9508582968697409
    - name: F1
      type: f1
      value: 0.9438690277313732
    - name: Accuracy
      type: accuracy
      value: 0.9868575969859305
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0598
- Precision: 0.9370
- Recall: 0.9509
- F1: 0.9439
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
| 0.0871        | 1.0   | 1756 | 0.0633          | 0.9197    | 0.9362 | 0.9279 | 0.9833   |
| 0.0386        | 2.0   | 3512 | 0.0572          | 0.9351    | 0.9483 | 0.9417 | 0.9866   |
| 0.0214        | 3.0   | 5268 | 0.0598          | 0.9370    | 0.9509 | 0.9439 | 0.9869   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.17.0
- Tokenizers 0.10.3
