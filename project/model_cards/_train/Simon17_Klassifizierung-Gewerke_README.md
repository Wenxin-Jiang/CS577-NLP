---
license: mit
tags:
- generated_from_trainer
metrics:
- f1
widget:
- text: "11025RLT601PU01SW01"
- text: "11004KAE906KR1BM04"
- text: "11004HZG201PU1SM02"
- text: "12064ISP005IS01SW09"
- text: "Störung HZG Pumpe"
model-index:
- name: Klassifizierung-Gewerke
  results: []
---


# Klassifizierung-Gewerke

This model is a fine-tuned version of [bert-base-german-cased](https://huggingface.co/bert-base-german-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0398
- F1: 0.9931

## Model description

The model is based on a BACnet data set and makes it possible to classify them according to trades.

## Intended uses & limitations

More information needed

## Training and evaluation data

The model is based on a German-based language dataset.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.1473        | 1.0   | 726  | 0.0952          | 0.9822 |
| 0.0252        | 2.0   | 1452 | 0.0488          | 0.9918 |
| 0.028         | 3.0   | 2178 | 0.0398          | 0.9931 |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1
