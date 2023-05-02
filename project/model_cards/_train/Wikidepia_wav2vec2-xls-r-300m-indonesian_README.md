---
language:
- id
license: apache-2.0
tags:
- automatic-speech-recognition
- hf-asr-leaderboard
- id
- mozilla-foundation/common_voice_8_0
- robust-speech-event
datasets:
- mozilla-foundation/common_voice_8_0
metrics:
- wer
- cer
model-index:
- name: XLS-R-300M - Indonesian
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: id
    metrics:
    - name: Test WER
      type: wer
      value: 5.046
    - name: Test CER
      type: cer
      value: 1.699
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: id
    metrics:
    - name: Test WER
      type: wer
      value: 41.31
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: id
    metrics:
    - name: Test WER
      type: wer
      value: 52.23
---

# Wav2Vec2 XLS-R-300M - Indonesian

This model is a fine-tuned version of `facebook/wav2vec2-xls-r-300m` on the `mozilla-foundation/common_voice_8_0` and [MagicHub Indonesian Conversational Speech Corpus](https://magichub.com/datasets/indonesian-conversational-speech-corpus/).

