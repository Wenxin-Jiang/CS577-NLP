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
- name: bert-base-uncased-finetuned-ner
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
      value: 0.9144678979771328
    - name: Recall
      type: recall
      value: 0.9305291419621882
    - name: F1
      type: f1
      value: 0.9224286110341003
    - name: Accuracy
      type: accuracy
      value: 0.9825726404753206
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-ner

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0618
- Precision: 0.9145
- Recall: 0.9305
- F1: 0.9224
- Accuracy: 0.9826

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 220  | 0.0809          | 0.8923    | 0.9051 | 0.8987 | 0.9784   |
| No log        | 2.0   | 440  | 0.0643          | 0.9108    | 0.9262 | 0.9184 | 0.9817   |
| 0.1657        | 3.0   | 660  | 0.0618          | 0.9145    | 0.9305 | 0.9224 | 0.9826   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.12.0
- Datasets 2.7.1
- Tokenizers 0.11.0
