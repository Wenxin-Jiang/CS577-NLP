---
license: mit
tags:
- generated_from_trainer
datasets:
- financial_phrasebank
metrics:
- accuracy
- f1
model-index:
- name: roberta-large-financial-phrasebank-allagree1
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: financial_phrasebank
      type: financial_phrasebank
      config: sentences_allagree
      split: train
      args: sentences_allagree
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9734513274336283
    - name: F1
      type: f1
      value: 0.9736033872259027
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-large-financial-phrasebank-allagree1

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on the financial_phrasebank dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1417
- Accuracy: 0.9735
- F1: 0.9736

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.503         | 1.0   | 227  | 0.2774          | 0.9513   | 0.9517 |
| 0.177         | 2.0   | 454  | 0.1518          | 0.9779   | 0.9778 |
| 0.0789        | 3.0   | 681  | 0.1364          | 0.9823   | 0.9822 |
| 0.0512        | 4.0   | 908  | 0.1131          | 0.9779   | 0.9778 |
| 0.03          | 5.0   | 1135 | 0.1417          | 0.9735   | 0.9736 |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
