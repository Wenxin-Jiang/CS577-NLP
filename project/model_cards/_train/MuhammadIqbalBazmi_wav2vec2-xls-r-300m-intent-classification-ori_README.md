---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: wav2vec2-xls-r-300m-intent-classification-ori
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-300m-intent-classification-ori

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3107
- Accuracy: 0.625

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 45

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.1982        | 1.0   | 14   | 2.1951          | 0.0625   |
| 2.2021        | 2.0   | 28   | 2.1847          | 0.1458   |
| 2.1819        | 3.0   | 42   | 2.1661          | 0.3333   |
| 2.1789        | 4.0   | 56   | 2.1413          | 0.3333   |
| 2.164         | 5.0   | 70   | 2.1183          | 0.3333   |
| 2.1484        | 6.0   | 84   | 2.0974          | 0.3333   |
| 2.1199        | 7.0   | 98   | 2.0939          | 0.3333   |
| 2.1343        | 8.0   | 112  | 2.0829          | 0.3333   |
| 2.1397        | 9.0   | 126  | 2.0654          | 0.3333   |
| 2.1045        | 10.0  | 140  | 2.0553          | 0.3333   |
| 2.1083        | 11.0  | 154  | 2.0255          | 0.3333   |
| 2.0914        | 12.0  | 168  | 2.0065          | 0.3333   |
| 2.0434        | 13.0  | 182  | 1.9696          | 0.3333   |
| 2.0687        | 14.0  | 196  | 1.9231          | 0.4167   |
| 2.0237        | 15.0  | 210  | 1.8679          | 0.4167   |
| 1.9562        | 16.0  | 224  | 1.8184          | 0.4167   |
| 2.0361        | 17.0  | 238  | 1.8803          | 0.3958   |
| 1.888         | 18.0  | 252  | 1.7802          | 0.4167   |
| 1.899         | 19.0  | 266  | 1.7662          | 0.4167   |
| 1.8959        | 20.0  | 280  | 1.7076          | 0.4167   |
| 1.8368        | 21.0  | 294  | 1.6566          | 0.4375   |
| 1.7358        | 22.0  | 308  | 1.6283          | 0.5      |
| 1.7877        | 23.0  | 322  | 1.6411          | 0.4583   |
| 1.7311        | 24.0  | 336  | 1.5525          | 0.5208   |
| 1.7079        | 25.0  | 350  | 1.5163          | 0.5      |
| 1.6496        | 26.0  | 364  | 1.5458          | 0.5      |
| 1.6374        | 27.0  | 378  | 1.5211          | 0.5      |
| 1.6048        | 28.0  | 392  | 1.4533          | 0.5417   |
| 1.5927        | 29.0  | 406  | 1.4319          | 0.5      |
| 1.4987        | 30.0  | 420  | 1.4579          | 0.5208   |
| 1.5745        | 31.0  | 434  | 1.4167          | 0.6042   |
| 1.4632        | 32.0  | 448  | 1.4471          | 0.5417   |
| 1.4686        | 33.0  | 462  | 1.4116          | 0.5625   |
| 1.5368        | 34.0  | 476  | 1.3872          | 0.6042   |
| 1.4327        | 35.0  | 490  | 1.3491          | 0.5833   |
| 1.3978        | 36.0  | 504  | 1.3325          | 0.5833   |
| 1.4509        | 37.0  | 518  | 1.3236          | 0.6042   |
| 1.3881        | 38.0  | 532  | 1.3426          | 0.5833   |
| 1.39          | 39.0  | 546  | 1.3137          | 0.6042   |
| 1.4153        | 40.0  | 560  | 1.3123          | 0.625    |
| 1.3635        | 41.0  | 574  | 1.3224          | 0.6042   |
| 1.403         | 42.0  | 588  | 1.3111          | 0.6042   |
| 1.3763        | 43.0  | 602  | 1.3197          | 0.5833   |
| 1.3539        | 44.0  | 616  | 1.3077          | 0.6042   |
| 1.306         | 45.0  | 630  | 1.3107          | 0.625    |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
