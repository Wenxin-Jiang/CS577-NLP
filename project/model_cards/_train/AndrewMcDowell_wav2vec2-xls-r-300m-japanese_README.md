---
language:
- ja
license: apache-2.0
tags:
- automatic-speech-recognition
- generated_from_trainer
- hf-asr-leaderboard
- ja
- mozilla-foundation/common_voice_8_0
- robust-speech-event
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: XLS-R-300-m
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: ja
    metrics:
    - name: Test WER
      type: wer
      value: 95.82
    - name: Test CER
      type: cer
      value: 23.64
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: de
    metrics:
    - name: Test WER
      type: wer
      value: 100.0
    - name: Test CER
      type: cer
      value: 30.99
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: ja
    metrics:
    - name: Test CER
      type: cer
      value: 30.37
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: ja
    metrics:
    - name: Test CER
      type: cer
      value: 34.42
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - JA dataset.

Kanji are converted into Hiragana using the [pykakasi](https://pykakasi.readthedocs.io/en/latest/index.html) library during training and evaluation. The model can output both Hiragana and Katakana characters. Since there is no spacing, WER is not a suitable metric for evaluating performance and CER is more suitable.

On mozilla-foundation/common_voice_8_0 it achieved:
- cer: 23.64%

On speech-recognition-community-v2/dev_data it achieved:
- cer: 30.99%

It achieves the following results on the evaluation set:
- Loss: 0.5212
- Wer: 1.3068

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
- train_batch_size: 48
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 50.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 4.0974        | 4.72  | 1000  | 4.0178          | 1.9535 |
| 2.1276        | 9.43  | 2000  | 0.9301          | 1.2128 |
| 1.7622        | 14.15 | 3000  | 0.7103          | 1.5527 |
| 1.6397        | 18.87 | 4000  | 0.6729          | 1.4269 |
| 1.5468        | 23.58 | 5000  | 0.6087          | 1.2497 |
| 1.4885        | 28.3  | 6000  | 0.5786          | 1.3222 |
| 1.451         | 33.02 | 7000  | 0.5726          | 1.3768 |
| 1.3912        | 37.74 | 8000  | 0.5518          | 1.2497 |
| 1.3617        | 42.45 | 9000  | 0.5352          | 1.2694 |
| 1.3113        | 47.17 | 10000 | 0.5228          | 1.2781 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0

#### Evaluation Commands
1. To evaluate on `mozilla-foundation/common_voice_8_0` with split `test`

```bash
python ./eval.py --model_id AndrewMcDowell/wav2vec2-xls-r-300m-japanese --dataset mozilla-foundation/common_voice_8_0 --config ja --split test --log_outputs
```

2. To evaluate on `mozilla-foundation/common_voice_8_0` with split `test`

```bash
python ./eval.py --model_id AndrewMcDowell/wav2vec2-xls-r-300m-japanese --dataset speech-recognition-community-v2/dev_data --config de --split validation --chunk_length_s 5.0 --stride_length_s 1.0
```