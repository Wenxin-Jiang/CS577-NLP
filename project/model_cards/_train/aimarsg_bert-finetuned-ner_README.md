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
      split: validation
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9307616221562809
    - name: Recall
      type: recall
      value: 0.9501851228542578
    - name: F1
      type: f1
      value: 0.9403730846102598
    - name: Accuracy
      type: accuracy
      value: 0.9859745687878966
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0638
- Precision: 0.9308
- Recall: 0.9502
- F1: 0.9404
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
| 0.0867        | 1.0   | 1756 | 0.0695          | 0.9266    | 0.9416 | 0.9341 | 0.9829   |
| 0.0338        | 2.0   | 3512 | 0.0604          | 0.9296    | 0.9495 | 0.9395 | 0.9860   |
| 0.0176        | 3.0   | 5268 | 0.0638          | 0.9308    | 0.9502 | 0.9404 | 0.9860   |


### Framework versions

- Transformers 4.26.0
- Pytorch 1.13.1+cu116
- Datasets 2.9.0
- Tokenizers 0.13.2
