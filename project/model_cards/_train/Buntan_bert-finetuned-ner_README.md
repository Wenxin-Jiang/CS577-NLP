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
      value: 0.9328604420983174
    - name: Recall
      type: recall
      value: 0.9516997643890945
    - name: F1
      type: f1
      value: 0.9421859380206598
    - name: Accuracy
      type: accuracy
      value: 0.986342497203744
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0612
- Precision: 0.9329
- Recall: 0.9517
- F1: 0.9422
- Accuracy: 0.9863

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
| 0.0904        | 1.0   | 1756 | 0.0686          | 0.9227    | 0.9355 | 0.9291 | 0.9820   |
| 0.0385        | 2.0   | 3512 | 0.0586          | 0.9381    | 0.9490 | 0.9435 | 0.9862   |
| 0.0215        | 3.0   | 5268 | 0.0612          | 0.9329    | 0.9517 | 0.9422 | 0.9863   |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.0+cu111
- Datasets 1.16.1
- Tokenizers 0.10.3
