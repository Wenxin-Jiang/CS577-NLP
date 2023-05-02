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
      value: 0.9341931216931217
    - name: Recall
      type: recall
      value: 0.9508582968697409
    - name: F1
      type: f1
      value: 0.9424520433694746
    - name: Accuracy
      type: accuracy
      value: 0.9865191028433508
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0603
- Precision: 0.9342
- Recall: 0.9509
- F1: 0.9425
- Accuracy: 0.9865

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
| 0.0854        | 1.0   | 1756 | 0.0633          | 0.9203    | 0.9364 | 0.9283 | 0.9830   |
| 0.034         | 2.0   | 3512 | 0.0626          | 0.9290    | 0.9493 | 0.9391 | 0.9863   |
| 0.0166        | 3.0   | 5268 | 0.0603          | 0.9342    | 0.9509 | 0.9425 | 0.9865   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
