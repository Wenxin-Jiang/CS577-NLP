---
license: apache-2.0
tags:
- automatic-speech-recognition
- NbAiLab/NPSC
- robust-speech-event
- false
- nb-NO
- hf-asr-leaderboard
datasets:
- NbAiLab/NPSC
language:
- nb-NO
model-index:
- name: wav2vec2-xls-r-1b-npsc-bokmaal-low-27k
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: NPSC
      type: NbAiLab/NPSC
      args: 16K_mp3_bokmaal
    metrics:
    - name: "Test (Bokm\xE5l) WER"
      type: wer
      value: 0.06332329423537675
    - name: "Test (Bokm\xE5l) CER"
      type: cer
      value: 0.02480899861950731
---

