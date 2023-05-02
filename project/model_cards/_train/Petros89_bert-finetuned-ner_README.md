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
      value: 0.9320436507936508
    - name: Recall
      type: recall
      value: 0.9486704813194211
    - name: F1
      type: f1
      value: 0.9402835696413678
    - name: Accuracy
      type: accuracy
      value: 0.9861217401542356
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0611
- Precision: 0.9320
- Recall: 0.9487
- F1: 0.9403
- Accuracy: 0.9861

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
| 0.0889        | 1.0   | 1756 | 0.0748          | 0.9060    | 0.9263 | 0.9160 | 0.9800   |
| 0.0381        | 2.0   | 3512 | 0.0631          | 0.9296    | 0.9468 | 0.9381 | 0.9855   |
| 0.0205        | 3.0   | 5268 | 0.0611          | 0.9320    | 0.9487 | 0.9403 | 0.9861   |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.7.0
- Datasets 2.4.0
- Tokenizers 0.12.1
