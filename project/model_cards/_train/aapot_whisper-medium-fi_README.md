---
language:
- fi
license: apache-2.0
tags:
- whisper-event
- finnish
datasets:
- mozilla-foundation/common_voice_11_0
- google/fleurs
metrics:
- wer
- cer
model-index:
- name: Whisper Medium Finnish
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11.0
      type: mozilla-foundation/common_voice_11_0
      config: fi
      split: test
      args: fi
    metrics:
    - name: Wer
      type: wer
      value: 11.71
    - name: Cer
      type: cer
      value: 2.12
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: FLEURS
      type: google/fleurs
      config: fi_fi
      split: test
      args: fi_fi
    metrics:
    - name: Wer
      type: wer
      value: 10.8
    - name: Cer
      type: cer
      value: 2.71
---