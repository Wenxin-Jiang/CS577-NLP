---
language:
- kk
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- kk
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-300m-kk-with-LM
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: ru
    metrics:
    - name: Test WER
      type: wer
      value: 0.4355
    - name: Test CER
      type: cer
      value: 0.10469915859660263
    - name: Test WER (+LM)
      type: wer
      value: 0.417
    - name: Test CER (+LM)
      type: cer
      value: 0.10319098269566598
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: kk
    metrics:
    - name: Test WER
      type: wer
      value: NA
    - name: Test CER
      type: cer
      value: NA
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8.0
      type: mozilla-foundation/common_voice_8_0
      args: kk
    metrics:
    - name: Test WER
      type: wer
      value: 41.7
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: kk
    metrics:
    - name: Test WER
      type: wer
      value: 67.09
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - KK dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7149
- Wer: 0.451

# Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py  --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-kk-with-LM  --dataset mozilla-foundation/common_voice_8_0 --config kk --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

Kazakh language isn't available in speech-recognition-community-v2/dev_data

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.000222
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 150.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 9.6799        | 9.09   | 200  | 3.6119          | 1.0    |
| 3.1332        | 18.18  | 400  | 2.5352          | 1.005  |
| 1.0465        | 27.27  | 600  | 0.6169          | 0.682  |
| 0.3452        | 36.36  | 800  | 0.6572          | 0.607  |
| 0.2575        | 45.44  | 1000 | 0.6527          | 0.578  |
| 0.2088        | 54.53  | 1200 | 0.6828          | 0.551  |
| 0.158         | 63.62  | 1400 | 0.7074          | 0.5575 |
| 0.1309        | 72.71  | 1600 | 0.6523          | 0.5595 |
| 0.1074        | 81.8   | 1800 | 0.7262          | 0.5415 |
| 0.087         | 90.89  | 2000 | 0.7199          | 0.521  |
| 0.0711        | 99.98  | 2200 | 0.7113          | 0.523  |
| 0.0601        | 109.09 | 2400 | 0.6863          | 0.496  |
| 0.0451        | 118.18 | 2600 | 0.6998          | 0.483  |
| 0.0378        | 127.27 | 2800 | 0.6971          | 0.4615 |
| 0.0319        | 136.36 | 3000 | 0.7119          | 0.4475 |
| 0.0305        | 145.44 | 3200 | 0.7181          | 0.459  |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0

### Evaluation Command

!python eval.py \
    --model_id DrishtiSharma/wav2vec2-xls-r-300m-kk-n2 \
    --dataset mozilla-foundation/common_voice_8_0 --config kk --split test --log_outputs