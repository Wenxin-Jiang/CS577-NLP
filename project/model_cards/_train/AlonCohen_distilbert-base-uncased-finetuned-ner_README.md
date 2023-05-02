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
      value: 0.9264510412051395
    - name: Recall
      type: recall
      value: 0.9356751314464705
    - name: F1
      type: f1
      value: 0.9310402404408081
    - name: Accuracy
      type: accuracy
      value: 0.9835417096922808
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0629
- Precision: 0.9265
- Recall: 0.9357
- F1: 0.9310
- Accuracy: 0.9835

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
| 0.2396        | 1.0   | 878  | 0.0706          | 0.9172    | 0.9186 | 0.9179 | 0.9810   |
| 0.0539        | 2.0   | 1756 | 0.0627          | 0.9264    | 0.9334 | 0.9299 | 0.9831   |
| 0.03          | 3.0   | 2634 | 0.0629          | 0.9265    | 0.9357 | 0.9310 | 0.9835   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
