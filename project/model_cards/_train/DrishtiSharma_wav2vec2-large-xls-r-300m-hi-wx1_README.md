---
language:
- hi
license: apache-2.0
tags:
- automatic-speech-recognition
- hf-asr-leaderboard
- robust-speech-event
datasets:
- mozilla-foundation/common_voice_7_0
metrics:
- wer
model-index:
- name: wav2vec2-large-xls-r-300m-hi-wx1
  results:
  - task:
      type: automatic-speech-recognition
      name: Speech Recognition
    dataset:
      type: mozilla-foundation/common_voice_7_0
      name: Common Voice 7
      args: hi
    metrics:
    - type: wer
      value: 37.19684845500431
      name: Test WER
    - name: Test CER
      type: cer
      value: 11.763235514672798
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-hi-wx1

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_7_0 -HI dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6552
- Wer: 0.3200

Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-hi-wx1 --dataset mozilla-foundation/common_voice_7_0 --config hi --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

NA

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.00024
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1800
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 12.2663       | 1.36  | 200  | 5.9245          | 1.0    |
| 4.1856        | 2.72  | 400  | 3.4968          | 1.0    |
| 3.3908        | 4.08  | 600  | 2.9970          | 1.0    |
| 1.5444        | 5.44  | 800  | 0.9071          | 0.6139 |
| 0.7237        | 6.8   | 1000 | 0.6508          | 0.4862 |
| 0.5323        | 8.16  | 1200 | 0.6217          | 0.4647 |
| 0.4426        | 9.52  | 1400 | 0.5785          | 0.4288 |
| 0.3933        | 10.88 | 1600 | 0.5935          | 0.4217 |
| 0.3532        | 12.24 | 1800 | 0.6358          | 0.4465 |
| 0.3319        | 13.6  | 2000 | 0.5789          | 0.4118 |
| 0.2877        | 14.96 | 2200 | 0.6163          | 0.4056 |
| 0.2663        | 16.33 | 2400 | 0.6176          | 0.3893 |
| 0.2511        | 17.68 | 2600 | 0.6065          | 0.3999 |
| 0.2275        | 19.05 | 2800 | 0.6183          | 0.3842 |
| 0.2098        | 20.41 | 3000 | 0.6486          | 0.3864 |
| 0.1943        | 21.77 | 3200 | 0.6365          | 0.3885 |
| 0.1877        | 23.13 | 3400 | 0.6013          | 0.3677 |
| 0.1679        | 24.49 | 3600 | 0.6451          | 0.3795 |
| 0.1667        | 25.85 | 3800 | 0.6410          | 0.3635 |
| 0.1514        | 27.21 | 4000 | 0.6000          | 0.3577 |
| 0.1453        | 28.57 | 4200 | 0.6020          | 0.3518 |
| 0.134         | 29.93 | 4400 | 0.6531          | 0.3517 |
| 0.1354        | 31.29 | 4600 | 0.6874          | 0.3578 |
| 0.1224        | 32.65 | 4800 | 0.6519          | 0.3492 |
| 0.1199        | 34.01 | 5000 | 0.6553          | 0.3490 |
| 0.1077        | 35.37 | 5200 | 0.6621          | 0.3429 |
| 0.0997        | 36.73 | 5400 | 0.6641          | 0.3413 |
| 0.0964        | 38.09 | 5600 | 0.6722          | 0.3385 |
| 0.0931        | 39.45 | 5800 | 0.6365          | 0.3363 |
| 0.0944        | 40.81 | 6000 | 0.6454          | 0.3326 |
| 0.0862        | 42.18 | 6200 | 0.6497          | 0.3256 |
| 0.0848        | 43.54 | 6400 | 0.6599          | 0.3226 |
| 0.0793        | 44.89 | 6600 | 0.6625          | 0.3232 |
| 0.076         | 46.26 | 6800 | 0.6463          | 0.3186 |
| 0.0749        | 47.62 | 7000 | 0.6559          | 0.3225 |
| 0.0663        | 48.98 | 7200 | 0.6552          | 0.3200 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
