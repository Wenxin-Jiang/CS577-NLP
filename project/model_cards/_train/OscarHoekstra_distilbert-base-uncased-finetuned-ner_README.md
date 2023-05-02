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
      value: 0.9274800708591674
    - name: Recall
      type: recall
      value: 0.9371294328224634
    - name: F1
      type: f1
      value: 0.9322797840966001
    - name: Accuracy
      type: accuracy
      value: 0.9841136193940935
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0586
- Precision: 0.9275
- Recall: 0.9371
- F1: 0.9323
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
| 0.2391        | 1.0   | 878  | 0.0706          | 0.9189    | 0.9230 | 0.9210 | 0.9813   |
| 0.054         | 2.0   | 1756 | 0.0576          | 0.9291    | 0.9370 | 0.9331 | 0.9841   |
| 0.0298        | 3.0   | 2634 | 0.0586          | 0.9275    | 0.9371 | 0.9323 | 0.9841   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.2
