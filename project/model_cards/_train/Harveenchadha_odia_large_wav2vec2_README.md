---
license: apache-2.0
language:
- or
tags:
- automatic-speech-recognition
- hf-asr-leaderboard
- model_for_talk
- mozilla-foundation/common_voice_7_0
- or
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
      args: or
    metrics:
    - name: Test WER
      type: wer
      value: 54.26
    - name: Test CER
      type: cer
      value: 11.36
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice-7.0
      type: mozilla-foundation/common_voice_7_0
      args: or
    metrics:
    - name: Test WER
      type: wer
      value: 53.58
    - name: Test CER
      type: cer
      value: 11.26
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice-8.0
      type: mozilla-foundation/common_voice_8_0
      args: or
    metrics:
    - name: Test WER
      type: wer
      value: 55.26
    - name: Test CER
      type: cer
      value: 13.01
---

