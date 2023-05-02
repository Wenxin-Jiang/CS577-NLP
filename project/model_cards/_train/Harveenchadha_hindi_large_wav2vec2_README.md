---
license: apache-2.0
language:
- hi
tags:
- automatic-speech-recognition
- hf-asr-leaderboard
- hi
- model_for_talk
- mozilla-foundation/common_voice_7_0
- robust-speech-event
datasets:
- Harveenchadha/indic-voice
model-index:
- name: Hindi Large
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice
      type: common_voice
      args: hi
    metrics:
    - name: Test WER
      type: wer
      value: 23.08
    - name: Test CER
      type: cer
      value: 8.11
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice-7.0
      type: mozilla-foundation/common_voice_7_0
      args: hi
    metrics:
    - name: Test WER
      type: wer
      value: 23.36
    - name: Test CER
      type: cer
      value: 8.94
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice-8.0
      type: mozilla-foundation/common_voice_8_0
      args: hi
    metrics:
    - name: Test WER
      type: wer
      value: 24.85
    - name: Test CER
      type: cer
      value: 9.99
---

