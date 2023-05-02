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
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9290544285555925
    - name: Recall
      type: recall
      value: 0.9375769101689228
    - name: F1
      type: f1
      value: 0.9332962138084633
    - name: Accuracy
      type: accuracy
      value: 0.9841136193940935
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0604
- Precision: 0.9291
- Recall: 0.9376
- F1: 0.9333
- Accuracy: 0.9841

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
| 0.2412        | 1.0   | 878  | 0.0688          | 0.9178    | 0.9246 | 0.9212 | 0.9815   |
| 0.0514        | 2.0   | 1756 | 0.0608          | 0.9251    | 0.9344 | 0.9298 | 0.9832   |
| 0.0304        | 3.0   | 2634 | 0.0604          | 0.9291    | 0.9376 | 0.9333 | 0.9841   |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0+cu111
- Datasets 1.12.1
- Tokenizers 0.10.3
