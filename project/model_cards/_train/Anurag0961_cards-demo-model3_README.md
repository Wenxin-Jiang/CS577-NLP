---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: cards-demo-model3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# cards-demo-model3

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9271
- F1: 0.7505

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
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.301         | 1.0   | 41   | 0.9127          | 0.7477 |
| 0.318         | 2.0   | 82   | 0.9173          | 0.7574 |
| 0.2757        | 3.0   | 123  | 0.9271          | 0.7505 |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Tokenizers 0.12.1
