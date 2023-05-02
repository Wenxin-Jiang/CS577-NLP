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
- name: test_ner-finetuned-ner
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
      value: 0.9242424242424242
    - name: Recall
      type: recall
      value: 0.9348920460901667
    - name: F1
      type: f1
      value: 0.9295367332183972
    - name: Accuracy
      type: accuracy
      value: 0.9834146186474335
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# test_ner-finetuned-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0623
- Precision: 0.9242
- Recall: 0.9349
- F1: 0.9295
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
| 0.2385        | 1.0   | 878  | 0.0708          | 0.9140    | 0.9216 | 0.9178 | 0.9808   |
| 0.055         | 2.0   | 1756 | 0.0626          | 0.9209    | 0.9340 | 0.9274 | 0.9828   |
| 0.0309        | 3.0   | 2634 | 0.0623          | 0.9242    | 0.9349 | 0.9295 | 0.9834   |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
