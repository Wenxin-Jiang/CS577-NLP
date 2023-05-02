---
language:
- hi
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_7_0
- generated_from_trainer
- hi
- robust-speech-event
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_7_0
model-index:
- name: wav2vec2-large-xls-r-300m-hi-CV7
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 7
      type: mozilla-foundation/common_voice_7_0
      args: hi
    metrics:
    - name: Test WER
      type: wer
      value: 35.31946325249292
    - name: Test CER
      type: cer
      value: 11.310803379493076
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: vot
    metrics:
    - name: Test WER
      type: wer
      value: NA
    - name: Test CER
      type: cer
      value: NA
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-hi-CV7

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_7_0 - HI dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6588
- Wer: 0.2987

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-hi-CV7 --dataset mozilla-foundation/common_voice_7_0 --config hi --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

NA

### Training hyperparameters

The following hyperparameters were used during training:
#
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 60
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 12.809        | 1.36  | 200  | 6.2066          | 1.0    |
| 4.3402        | 2.72  | 400  | 3.5184          | 1.0    |
| 3.4365        | 4.08  | 600  | 3.2779          | 1.0    |
| 1.8643        | 5.44  | 800  | 0.9875          | 0.6270 |
| 0.7504        | 6.8   | 1000 | 0.6382          | 0.4666 |
| 0.5328        | 8.16  | 1200 | 0.6075          | 0.4505 |
| 0.4364        | 9.52  | 1400 | 0.5785          | 0.4215 |
| 0.3777        | 10.88 | 1600 | 0.6279          | 0.4227 |
| 0.3374        | 12.24 | 1800 | 0.6536          | 0.4192 |
| 0.3236        | 13.6  | 2000 | 0.5911          | 0.4047 |
| 0.2877        | 14.96 | 2200 | 0.5955          | 0.4097 |
| 0.2643        | 16.33 | 2400 | 0.5923          | 0.3744 |
| 0.2421        | 17.68 | 2600 | 0.6307          | 0.3814 |
| 0.2218        | 19.05 | 2800 | 0.6036          | 0.3764 |
| 0.2046        | 20.41 | 3000 | 0.6286          | 0.3797 |
| 0.191         | 21.77 | 3200 | 0.6517          | 0.3889 |
| 0.1856        | 23.13 | 3400 | 0.6193          | 0.3661 |
| 0.1721        | 24.49 | 3600 | 0.7034          | 0.3727 |
| 0.1656        | 25.85 | 3800 | 0.6293          | 0.3591 |
| 0.1532        | 27.21 | 4000 | 0.6075          | 0.3611 |
| 0.1507        | 28.57 | 4200 | 0.6313          | 0.3565 |
| 0.1381        | 29.93 | 4400 | 0.6564          | 0.3578 |
| 0.1359        | 31.29 | 4600 | 0.6724          | 0.3543 |
| 0.1248        | 32.65 | 4800 | 0.6789          | 0.3512 |
| 0.1198        | 34.01 | 5000 | 0.6442          | 0.3539 |
| 0.1125        | 35.37 | 5200 | 0.6676          | 0.3419 |
| 0.1036        | 36.73 | 5400 | 0.7017          | 0.3435 |
| 0.0982        | 38.09 | 5600 | 0.6828          | 0.3319 |
| 0.0971        | 39.45 | 5800 | 0.6112          | 0.3351 |
| 0.0968        | 40.81 | 6000 | 0.6424          | 0.3252 |
| 0.0893        | 42.18 | 6200 | 0.6707          | 0.3304 |
| 0.0878        | 43.54 | 6400 | 0.6432          | 0.3236 |
| 0.0827        | 44.89 | 6600 | 0.6696          | 0.3240 |
| 0.0788        | 46.26 | 6800 | 0.6564          | 0.3180 |
| 0.0753        | 47.62 | 7000 | 0.6574          | 0.3130 |
| 0.0674        | 48.98 | 7200 | 0.6698          | 0.3175 |
| 0.0676        | 50.34 | 7400 | 0.6441          | 0.3142 |
| 0.0626        | 51.7  | 7600 | 0.6642          | 0.3121 |
| 0.0617        | 53.06 | 7800 | 0.6615          | 0.3117 |
| 0.0599        | 54.42 | 8000 | 0.6634          | 0.3059 |
| 0.0538        | 55.78 | 8200 | 0.6464          | 0.3033 |
| 0.0571        | 57.14 | 8400 | 0.6503          | 0.3018 |
| 0.0491        | 58.5  | 8600 | 0.6625          | 0.3025 |
| 0.0511        | 59.86 | 8800 | 0.6588          | 0.2987 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
