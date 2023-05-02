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
      value: 0.9260322366968425
    - name: Recall
      type: recall
      value: 0.9383599955252265
    - name: F1
      type: f1
      value: 0.9321553592265377
    - name: Accuracy
      type: accuracy
      value: 0.9834146186474335
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0607
- Precision: 0.9260
- Recall: 0.9384
- F1: 0.9322
- Accuracy: 0.9834

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
| 0.2545        | 1.0   | 878  | 0.0711          | 0.9096    | 0.9214 | 0.9154 | 0.9800   |
| 0.0555        | 2.0   | 1756 | 0.0593          | 0.9185    | 0.9356 | 0.9270 | 0.9827   |
| 0.0297        | 3.0   | 2634 | 0.0607          | 0.9260    | 0.9384 | 0.9322 | 0.9834   |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
