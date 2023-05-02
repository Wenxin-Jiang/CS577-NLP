---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: distilbert-base-uncased-finetuned-emotion
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-emotion

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2055
- Accuracy: 0.9355
- F1: 0.9354

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.1775        | 1.0   | 250  | 0.1765          | 0.929    | 0.9287 |
| 0.1205        | 2.0   | 500  | 0.1516          | 0.9395   | 0.9393 |
| 0.0981        | 3.0   | 750  | 0.1530          | 0.9345   | 0.9351 |
| 0.0799        | 4.0   | 1000 | 0.1654          | 0.935    | 0.9348 |
| 0.0641        | 5.0   | 1250 | 0.1638          | 0.937    | 0.9364 |
| 0.0495        | 6.0   | 1500 | 0.1695          | 0.937    | 0.9369 |
| 0.0417        | 7.0   | 1750 | 0.1873          | 0.935    | 0.9350 |
| 0.0332        | 8.0   | 2000 | 0.1941          | 0.935    | 0.9351 |
| 0.0275        | 9.0   | 2250 | 0.1977          | 0.9385   | 0.9385 |
| 0.0224        | 10.0  | 2500 | 0.2055          | 0.9355   | 0.9354 |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.11.0
- Datasets 1.16.1
- Tokenizers 0.10.3
