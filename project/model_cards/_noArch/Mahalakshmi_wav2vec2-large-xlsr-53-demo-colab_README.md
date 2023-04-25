---
language:
- ne
license: apache-2.0
tags:
- automatic-speech-recognition
- robust-speech-event
- hf-asr-leaderboard
datasets:
- openslr
model-index:
- name: wav2vec2-large-xlsr-53-tamil
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: openslr
      type: openslr
      args: ne
    metrics:
    - name: Test WER
      type: wer
      value: 25.02
---

#xlsr-large-53-tamil