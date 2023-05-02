---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- pawsx
metrics:
- accuracy
- f1
model-index:
- name: distilbert-base-uncased-finetuned-paws
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: pawsx
      type: pawsx
      args: en
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8355
    - name: F1
      type: f1
      value: 0.8361579553422098
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-paws

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the pawsx dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3850
- Accuracy: 0.8355
- F1: 0.8362

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.6715        | 1.0   | 772  | 0.5982          | 0.6785   | 0.6799 |
| 0.4278        | 2.0   | 1544 | 0.3850          | 0.8355   | 0.8362 |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.12.1+cu113
- Datasets 1.16.1
- Tokenizers 0.10.3
