---
license: apache-2.0
tags:
- generated_from_trainer
- automatic-speech-recognition
- NbAiLab/NPSC
- robust-speech-event
- false
- nn-NO
- hf-asr-leaderboard
datasets:
- NbAiLab/NPSC
language:
- nn-NO
model-index:
- name: XLSR-300M-nynorsk
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: NPSC
      type: NbAiLab/NPSC
      args: 16K_mp3_nynorsk
    metrics:
    - name: Test (Nynorsk) WER
      type: wer
      value: 0.12136286840623241
    - name: Test (Nynorsk) CER
      type: cer
      value: 0.041988362534453025
---

