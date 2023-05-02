---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: distilbert-finetuned-fakenews
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-finetuned-fakenews

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0049
- Accuracy: 0.9995
- F1: 0.9995

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.0392        | 1.0   | 500  | 0.0059          | 0.999    | 0.999  |
| 0.002         | 2.0   | 1000 | 0.0047          | 0.9995   | 0.9995 |
| 0.0001        | 3.0   | 1500 | 0.0047          | 0.9995   | 0.9995 |
| 0.0001        | 4.0   | 2000 | 0.0049          | 0.9995   | 0.9995 |
| 0.0           | 5.0   | 2500 | 0.0049          | 0.9995   | 0.9995 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.12.0
