---
language:
- bg
license: apache-2.0
tags:
- automatic-speech-recognition
- bg
- generated_from_trainer
- hf-asr-leaderboard
- mozilla-foundation/common_voice_8_0
- robust-speech-event
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-300m-bg-d2
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: bg
    metrics:
    - name: Test WER
      type: wer
      value: 0.28775471338792613
    - name: Test CER
      type: cer
      value: 0.06861971204625049
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: bg
    metrics:
    - name: Test WER
      type: wer
      value: 0.49783147459727384
    - name: Test CER
      type: cer
      value: 0.1591062599627158
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: bg
    metrics:
    - name: Test WER
      type: wer
      value: 51.25
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-bg-d2

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - BG dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3421
- Wer: 0.2860

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-bg-d2 --dataset mozilla-foundation/common_voice_8_0 --config bg --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-bg-d2 --dataset speech-recognition-community-v2/dev_data --config bg --split validation --chunk_length_s 10 --stride_length_s 1
    
### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.00025
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 700
- num_epochs: 35
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 6.8791        | 1.74  | 200  | 3.1902          | 1.0    |
| 3.0441        | 3.48  | 400  | 2.8098          | 0.9864 |
| 1.1499        | 5.22  | 600  | 0.4668          | 0.5014 |
| 0.4968        | 6.96  | 800  | 0.4162          | 0.4472 |
| 0.3553        | 8.7   | 1000 | 0.3580          | 0.3777 |
| 0.3027        | 10.43 | 1200 | 0.3422          | 0.3506 |
| 0.2562        | 12.17 | 1400 | 0.3556          | 0.3639 |
| 0.2272        | 13.91 | 1600 | 0.3621          | 0.3583 |
| 0.2125        | 15.65 | 1800 | 0.3436          | 0.3358 |
| 0.1904        | 17.39 | 2000 | 0.3650          | 0.3545 |
| 0.1695        | 19.13 | 2200 | 0.3366          | 0.3241 |
| 0.1532        | 20.87 | 2400 | 0.3550          | 0.3311 |
| 0.1453        | 22.61 | 2600 | 0.3582          | 0.3131 |
| 0.1359        | 24.35 | 2800 | 0.3524          | 0.3084 |
| 0.1233        | 26.09 | 3000 | 0.3503          | 0.2973 |
| 0.1114        | 27.83 | 3200 | 0.3434          | 0.2946 |
| 0.1051        | 29.57 | 3400 | 0.3474          | 0.2956 |
| 0.0965        | 31.3  | 3600 | 0.3426          | 0.2907 |
| 0.0923        | 33.04 | 3800 | 0.3478          | 0.2894 |
| 0.0894        | 34.78 | 4000 | 0.3421          | 0.2860 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
