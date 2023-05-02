---
tags:
- generated_from_trainer
model-index:
- name: finetuning-1-12-2022
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuning-1-12-2022

This model is a fine-tuned version of [ASR/Finetuning](https://huggingface.co/ASR/Finetuning) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0357
- Wer: 0.0836

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 50

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| No log        | 1.0   | 45   | 2.6669          | 1.0    |
| No log        | 2.0   | 90   | 1.4650          | 0.9652 |
| No log        | 3.0   | 135  | 0.8614          | 0.7491 |
| No log        | 4.0   | 180  | 0.8031          | 0.7735 |
| No log        | 5.0   | 225  | 0.7993          | 0.7909 |
| No log        | 6.0   | 270  | 0.5708          | 0.6411 |
| No log        | 7.0   | 315  | 0.5728          | 0.7178 |
| No log        | 8.0   | 360  | 0.5439          | 0.6341 |
| 1.2911        | 9.0   | 405  | 0.5072          | 0.7213 |
| 1.2911        | 10.0  | 450  | 0.3578          | 0.5331 |
| 1.2911        | 11.0  | 495  | 0.4871          | 0.6411 |
| 1.2911        | 12.0  | 540  | 0.3034          | 0.4634 |
| 1.2911        | 13.0  | 585  | 0.4684          | 0.6028 |
| 1.2911        | 14.0  | 630  | 0.2638          | 0.4216 |
| 1.2911        | 15.0  | 675  | 0.2657          | 0.4948 |
| 1.2911        | 16.0  | 720  | 0.2593          | 0.3972 |
| 1.2911        | 17.0  | 765  | 0.2770          | 0.4634 |
| 0.3079        | 18.0  | 810  | 0.2936          | 0.4530 |
| 0.3079        | 19.0  | 855  | 0.4168          | 0.5436 |
| 0.3079        | 20.0  | 900  | 0.2642          | 0.3693 |
| 0.3079        | 21.0  | 945  | 0.1827          | 0.3519 |
| 0.3079        | 22.0  | 990  | 0.1807          | 0.2962 |
| 0.3079        | 23.0  | 1035 | 0.2134          | 0.3484 |
| 0.3079        | 24.0  | 1080 | 0.1317          | 0.2474 |
| 0.3079        | 25.0  | 1125 | 0.0950          | 0.2021 |
| 0.3079        | 26.0  | 1170 | 0.0985          | 0.1707 |
| 0.1678        | 27.0  | 1215 | 0.1444          | 0.2753 |
| 0.1678        | 28.0  | 1260 | 0.0816          | 0.1289 |
| 0.1678        | 29.0  | 1305 | 0.1103          | 0.1916 |
| 0.1678        | 30.0  | 1350 | 0.0878          | 0.1777 |
| 0.1678        | 31.0  | 1395 | 0.1436          | 0.1568 |
| 0.1678        | 32.0  | 1440 | 0.1097          | 0.1882 |
| 0.1678        | 33.0  | 1485 | 0.0995          | 0.1777 |
| 0.1678        | 34.0  | 1530 | 0.0917          | 0.1882 |
| 0.1678        | 35.0  | 1575 | 0.0691          | 0.1254 |
| 0.0743        | 36.0  | 1620 | 0.0394          | 0.0941 |
| 0.0743        | 37.0  | 1665 | 0.0592          | 0.1185 |
| 0.0743        | 38.0  | 1710 | 0.0680          | 0.1220 |
| 0.0743        | 39.0  | 1755 | 0.0748          | 0.0941 |
| 0.0743        | 40.0  | 1800 | 0.0651          | 0.1010 |
| 0.0743        | 41.0  | 1845 | 0.0688          | 0.1045 |
| 0.0743        | 42.0  | 1890 | 0.0489          | 0.0871 |
| 0.0743        | 43.0  | 1935 | 0.0524          | 0.0976 |
| 0.0743        | 44.0  | 1980 | 0.0415          | 0.1080 |
| 0.0234        | 45.0  | 2025 | 0.0489          | 0.0767 |
| 0.0234        | 46.0  | 2070 | 0.0337          | 0.0732 |
| 0.0234        | 47.0  | 2115 | 0.0456          | 0.0662 |
| 0.0234        | 48.0  | 2160 | 0.0326          | 0.0871 |
| 0.0234        | 49.0  | 2205 | 0.0319          | 0.0976 |
| 0.0234        | 50.0  | 2250 | 0.0357          | 0.0836 |


### Framework versions

- Transformers 4.23.0
- Pytorch 1.13.0+cpu
- Datasets 2.5.2
- Tokenizers 0.13.1
