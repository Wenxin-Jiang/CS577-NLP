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
      value: 0.9239501818582607
    - name: Recall
      type: recall
      value: 0.9378006488421524
    - name: F1
      type: f1
      value: 0.9308238951809905
    - name: Accuracy
      type: accuracy
      value: 0.9837800054013695
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0596
- Precision: 0.9240
- Recall: 0.9378
- F1: 0.9308
- Accuracy: 0.9838

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
| 0.2381        | 1.0   | 878  | 0.0707          | 0.9100    | 0.9240 | 0.9170 | 0.9805   |
| 0.0563        | 2.0   | 1756 | 0.0583          | 0.9246    | 0.9382 | 0.9314 | 0.9835   |
| 0.03          | 3.0   | 2634 | 0.0596          | 0.9240    | 0.9378 | 0.9308 | 0.9838   |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
