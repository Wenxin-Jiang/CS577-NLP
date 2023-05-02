---
language:
- fr
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- robust-speech-event
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: XLS-R-1B - French
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: fr
    metrics:
    - name: Test WER (with LM)
      type: wer
      value: 15.4
    - name: Test CER (with LM)
      type: cer
      value: 5.36
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: fr
    metrics:
    - name: Test WER (with LM)
      type: wer
      value: 25.05
    - name: Test CER (with LM)
      type: cer
      value: 12.45
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: fr
    metrics:
    - name: Test WER
      type: wer
      value: 27.1
---

## Model description

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-1b](https://huggingface.co/facebook/wav2vec2-xls-r-1b) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - FR dataset.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 6.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 0.9827        | 0.29  | 1000  | inf             | 0.2937 |
| 1.0203        | 0.57  | 2000  | inf             | 0.2711 |
| 1.0048        | 0.86  | 3000  | inf             | 0.2620 |
| 0.9858        | 1.15  | 4000  | inf             | 0.2522 |
| 0.9709        | 1.43  | 5000  | inf             | 0.2365 |
| 0.9347        | 1.72  | 6000  | inf             | 0.2332 |
| 0.9256        | 2.01  | 7000  | inf             | 0.2261 |
| 0.8936        | 2.29  | 8000  | inf             | 0.2203 |
| 0.877         | 2.58  | 9000  | inf             | 0.2096 |
| 0.8393        | 2.87  | 10000 | inf             | 0.2017 |
| 0.8156        | 3.15  | 11000 | inf             | 0.1936 |
| 0.8015        | 3.44  | 12000 | inf             | 0.1880 |
| 0.774         | 3.73  | 13000 | inf             | 0.1834 |
| 0.8372        | 4.01  | 14000 | inf             | 0.1934 |
| 0.8075        | 4.3   | 15000 | inf             | 0.1923 |
| 0.8069        | 4.59  | 16000 | inf             | 0.1877 |
| 0.8064        | 4.87  | 17000 | inf             | 0.1955 |
| 0.801         | 5.16  | 18000 | inf             | 0.1891 |
| 0.8022        | 5.45  | 19000 | inf             | 0.1895 |
| 0.792         | 5.73  | 20000 | inf             | 0.1854 |

It achieves the best result on the validation set on STEP 13000:
- Wer: 0.1834

Some problem occurs when calculating the validation loss.

### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3.dev0
- Tokenizers 0.11.0

### Evaluation Commands
1. To evaluate on `mozilla-foundation/common_voice_8` with split `test`
```bash
python eval.py --model_id Plim/xls-r-1b-cv_8-fr --dataset mozilla-foundation/common_voice_8_0 --config fr --split test
```
2. To evaluate on `speech-recognition-community-v2/dev_data`
```bash
python eval.py --model_id Plim/xls-r-1b-cv_8-fr --dataset speech-recognition-community-v2/dev_data --config fr --split validation --chunk_length_s 5.0 --stride_length_s 1.0
```

### Evaluation Results

Without LM:

| Dataset    | WER   | CER   |
|:----------:|:-----:|:-----:|
| TEST CV    | 18.33 | 5.60  |
| DEV audio  | 31.33 | 13.20 |
| TEST audio | /     | /     |

With LM:

| Dataset    | WER   | CER   |
|:----------:|:-----:|:-----:|
| TEST CV    | 15.40 | 5.36  |
| DEV audio  | 25.05 | 12.45 |
| TEST audio | /     | /     |
