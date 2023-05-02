---
language:
- ur
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- ur
- robust-speech-event
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: ''
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8.0
      type: mozilla-foundation/common_voice_8_0
      args: ur
    metrics:
    - name: Test WER
      type: wer
      value: 47.38
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [HarrisDePerceptron/xls-r-300m-ur](https://huggingface.co/HarrisDePerceptron/xls-r-300m-ur) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - UR dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0517
- WER: 0.5151291512915129
- CER: 0.23689640940982254

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 100.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 1.2991        | 1.96  | 100  | 0.9769          | 0.6627 |
| 1.3415        | 3.92  | 200  | 0.9701          | 0.6594 |
| 1.2998        | 5.88  | 300  | 0.9678          | 0.6668 |
| 1.2881        | 7.84  | 400  | 0.9650          | 0.6613 |
| 1.2369        | 9.8   | 500  | 0.9392          | 0.6502 |
| 1.2293        | 11.76 | 600  | 0.9536          | 0.6480 |
| 1.1709        | 13.73 | 700  | 0.9265          | 0.6402 |
| 1.1492        | 15.69 | 800  | 0.9636          | 0.6506 |
| 1.1044        | 17.65 | 900  | 0.9305          | 0.6351 |
| 1.0704        | 19.61 | 1000 | 0.9329          | 0.6280 |
| 1.0039        | 21.57 | 1100 | 0.9413          | 0.6295 |
| 0.9756        | 23.53 | 1200 | 0.9718          | 0.6185 |
| 0.9633        | 25.49 | 1300 | 0.9731          | 0.6133 |
| 0.932         | 27.45 | 1400 | 0.9659          | 0.6199 |
| 0.9252        | 29.41 | 1500 | 0.9766          | 0.6196 |
| 0.9172        | 31.37 | 1600 | 1.0052          | 0.6199 |
| 0.8733        | 33.33 | 1700 | 0.9955          | 0.6203 |
| 0.868         | 35.29 | 1800 | 1.0069          | 0.6240 |
| 0.8547        | 37.25 | 1900 | 0.9783          | 0.6258 |
| 0.8451        | 39.22 | 2000 | 0.9845          | 0.6052 |
| 0.8374        | 41.18 | 2100 | 0.9496          | 0.6137 |
| 0.8153        | 43.14 | 2200 | 0.9756          | 0.6122 |
| 0.8134        | 45.1  | 2300 | 0.9712          | 0.6096 |
| 0.8019        | 47.06 | 2400 | 0.9565          | 0.5970 |
| 0.7746        | 49.02 | 2500 | 0.9864          | 0.6096 |
| 0.7664        | 50.98 | 2600 | 0.9988          | 0.6092 |
| 0.7708        | 52.94 | 2700 | 1.0181          | 0.6255 |
| 0.7468        | 54.9  | 2800 | 0.9918          | 0.6148 |
| 0.7241        | 56.86 | 2900 | 1.0150          | 0.6018 |
| 0.7165        | 58.82 | 3000 | 1.0439          | 0.6063 |
| 0.7104        | 60.78 | 3100 | 1.0016          | 0.6037 |
| 0.6954        | 62.75 | 3200 | 1.0117          | 0.5970 |
| 0.6753        | 64.71 | 3300 | 1.0191          | 0.6037 |
| 0.6803        | 66.67 | 3400 | 1.0190          | 0.6033 |
| 0.661         | 68.63 | 3500 | 1.0284          | 0.6007 |
| 0.6597        | 70.59 | 3600 | 1.0060          | 0.5967 |
| 0.6398        | 72.55 | 3700 | 1.0372          | 0.6048 |
| 0.6105        | 74.51 | 3800 | 1.0048          | 0.6044 |
| 0.6164        | 76.47 | 3900 | 1.0398          | 0.6148 |
| 0.6354        | 78.43 | 4000 | 1.0272          | 0.6133 |
| 0.5952        | 80.39 | 4100 | 1.0364          | 0.6081 |
| 0.5814        | 82.35 | 4200 | 1.0418          | 0.6092 |
| 0.6079        | 84.31 | 4300 | 1.0277          | 0.5967 |
| 0.5748        | 86.27 | 4400 | 1.0362          | 0.6041 |
| 0.5624        | 88.24 | 4500 | 1.0427          | 0.6007 |
| 0.5767        | 90.2  | 4600 | 1.0370          | 0.5919 |
| 0.5793        | 92.16 | 4700 | 1.0442          | 0.6011 |
| 0.547         | 94.12 | 4800 | 1.0516          | 0.5982 |
| 0.5513        | 96.08 | 4900 | 1.0461          | 0.5989 |
| 0.5429        | 98.04 | 5000 | 1.0504          | 0.5996 |
| 0.5404        | 100.0 | 5100 | 1.0517          | 0.5967 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0
