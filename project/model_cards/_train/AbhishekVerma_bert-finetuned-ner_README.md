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
      value: 0.9325508348487354
    - name: Recall
      type: recall
      value: 0.9493436553349041
    - name: F1
      type: f1
      value: 0.9408723209073472
    - name: Accuracy
      type: accuracy
      value: 0.9862247601106728
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0604
- Precision: 0.9326
- Recall: 0.9493
- F1: 0.9409
- Accuracy: 0.9862

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
| 0.0902        | 1.0   | 1756 | 0.0673          | 0.9151    | 0.9308 | 0.9229 | 0.9823   |
| 0.0347        | 2.0   | 3512 | 0.0613          | 0.9265    | 0.9478 | 0.9370 | 0.9856   |
| 0.0181        | 3.0   | 5268 | 0.0604          | 0.9326    | 0.9493 | 0.9409 | 0.9862   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.2
