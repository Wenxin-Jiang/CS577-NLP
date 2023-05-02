---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: hf_trainer
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hf_trainer

This model is a fine-tuned version of [distilbert-base-multilingual-cased](https://huggingface.co/distilbert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0708
- F1: 0.9066

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.0344        | 1.0   | 565  | 0.0661          | 0.8811 |
| 0.0354        | 2.0   | 1130 | 0.0641          | 0.8963 |
| 0.0222        | 3.0   | 1695 | 0.0690          | 0.8994 |
| 0.0145        | 4.0   | 2260 | 0.0714          | 0.9036 |
| 0.011         | 5.0   | 2825 | 0.0708          | 0.9066 |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1
