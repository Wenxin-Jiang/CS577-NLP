---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: idp-headers
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# idp-headers

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6714
- F1: 0.4823

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
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 1.7995        | 1.0   | 5    | 1.8557          | 0.1629 |
| 1.7125        | 2.0   | 10   | 1.7832          | 0.1759 |
| 1.6381        | 3.0   | 15   | 1.7243          | 0.4698 |
| 1.5746        | 4.0   | 20   | 1.6857          | 0.4823 |
| 1.5354        | 5.0   | 25   | 1.6714          | 0.4823 |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Tokenizers 0.12.1
