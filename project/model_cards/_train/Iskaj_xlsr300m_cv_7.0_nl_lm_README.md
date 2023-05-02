---
language:
- nl
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- nl
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: XLS-R-300M - Dutch
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8 NL
      type: mozilla-foundation/common_voice_8_0
      args: nl
    metrics:
    - name: Test WER
      type: wer
      value: 32
    - name: Test CER
      type: cer
      value: 17
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: nl
    metrics:
    - name: Test WER
      type: wer
      value: 37.44
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: nl
    metrics:
    - name: Test WER
      type: wer
      value: 38.74
---
# xlsr300m_cv_7.0_nl_lm