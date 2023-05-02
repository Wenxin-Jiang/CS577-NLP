---
license: cc
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: racism-finetuned-detests-prueba
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# racism-finetuned-detests-prueba

This model is a fine-tuned version of [davidmasip/racism](https://huggingface.co/davidmasip/racism) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3034
- F1: 0.6222

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
- train_batch_size: 50
- eval_batch_size: 50
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.0001        | 1.0   | 49   | 1.0331          | 0.6667 |
| 0.0           | 2.0   | 98   | 1.2473          | 0.5992 |
| 0.0           | 3.0   | 147  | 1.2280          | 0.6227 |
| 0.0           | 4.0   | 196  | 1.2530          | 0.6245 |
| 0.0           | 5.0   | 245  | 1.2708          | 0.6222 |
| 0.0           | 6.0   | 294  | 1.2827          | 0.6222 |
| 0.0           | 7.0   | 343  | 1.2918          | 0.6222 |
| 0.0           | 8.0   | 392  | 1.2982          | 0.6222 |
| 0.0           | 9.0   | 441  | 1.3021          | 0.6222 |
| 0.0           | 10.0  | 490  | 1.3034          | 0.6222 |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
