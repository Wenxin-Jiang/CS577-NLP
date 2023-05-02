---
language:
- fi
license: apache-2.0
tags:
- whisper-event
datasets:
- mozilla-foundation/common_voice_11_0
- facebook/voxpopuli
- google/fleurs
metrics:
- wer
model-index:
- name: TeemuSo/whisper-large-fi
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0
      type: mozilla-foundation/common_voice_11_0
      config: fi
      split: test
    metrics:
    - type: wer
      value: 14.24
      name: WER
---