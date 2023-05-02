---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-16-8
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-16-8

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6915
- Accuracy: 0.6579

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.7129        | 1.0   | 7    | 0.7309          | 0.2857   |
| 0.6549        | 2.0   | 14   | 0.7316          | 0.4286   |
| 0.621         | 3.0   | 21   | 0.7131          | 0.5714   |
| 0.3472        | 4.0   | 28   | 0.5703          | 0.4286   |
| 0.2041        | 5.0   | 35   | 0.6675          | 0.5714   |
| 0.031         | 6.0   | 42   | 1.6750          | 0.5714   |
| 0.0141        | 7.0   | 49   | 1.8743          | 0.5714   |
| 0.0055        | 8.0   | 56   | 1.1778          | 0.5714   |
| 0.0024        | 9.0   | 63   | 1.0699          | 0.5714   |
| 0.0019        | 10.0  | 70   | 1.0933          | 0.5714   |
| 0.0012        | 11.0  | 77   | 1.1218          | 0.7143   |
| 0.0007        | 12.0  | 84   | 1.1468          | 0.7143   |
| 0.0006        | 13.0  | 91   | 1.1584          | 0.7143   |
| 0.0006        | 14.0  | 98   | 1.3092          | 0.7143   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
