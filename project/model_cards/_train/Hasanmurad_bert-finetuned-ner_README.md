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
      value: 0.9363425925925926
    - name: Recall
      type: recall
      value: 0.9530461124200605
    - name: F1
      type: f1
      value: 0.9446205170975813
    - name: Accuracy
      type: accuracy
      value: 0.986769294166127
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0774
- Precision: 0.9363
- Recall: 0.9530
- F1: 0.9446
- Accuracy: 0.9868

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
| 0.0273        | 1.0   | 1756 | 0.0787          | 0.9286    | 0.9411 | 0.9348 | 0.9845   |
| 0.0141        | 2.0   | 3512 | 0.0772          | 0.9299    | 0.9504 | 0.9400 | 0.9863   |
| 0.0054        | 3.0   | 5268 | 0.0774          | 0.9363    | 0.9530 | 0.9446 | 0.9868   |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1
