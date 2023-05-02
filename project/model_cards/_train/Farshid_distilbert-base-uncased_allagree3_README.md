---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- financial_phrasebank
metrics:
- accuracy
- f1
model-index:
- name: distilbert-base-uncased_allagree3
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: financial_phrasebank
      type: financial_phrasebank
      args: sentences_allagree
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9778761061946902
    - name: F1
      type: f1
      value: 0.9780006392634297
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased_allagree3

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the financial_phrasebank dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0937
- Accuracy: 0.9779
- F1: 0.9780

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.6418        | 1.0   | 57   | 0.3340          | 0.8805   | 0.8768 |
| 0.1821        | 2.0   | 114  | 0.1088          | 0.9690   | 0.9691 |
| 0.0795        | 3.0   | 171  | 0.0822          | 0.9823   | 0.9823 |
| 0.0385        | 4.0   | 228  | 0.0939          | 0.9646   | 0.9646 |
| 0.0218        | 5.0   | 285  | 0.1151          | 0.9735   | 0.9737 |
| 0.0149        | 6.0   | 342  | 0.1126          | 0.9690   | 0.9694 |
| 0.006         | 7.0   | 399  | 0.0989          | 0.9779   | 0.9780 |
| 0.0093        | 8.0   | 456  | 0.1009          | 0.9779   | 0.9780 |
| 0.0063        | 9.0   | 513  | 0.0899          | 0.9779   | 0.9780 |
| 0.0039        | 10.0  | 570  | 0.0937          | 0.9779   | 0.9780 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cpu
- Datasets 2.3.2
- Tokenizers 0.12.1
