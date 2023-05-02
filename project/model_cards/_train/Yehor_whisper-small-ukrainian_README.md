---
language:
- uk
license: mit
tags:
- whisper-event
datasets:
- Yehor/voa-uk-transcriptions
metrics:
- wer
model-index:
- name: Whisper Small Ukranian
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_10_0 uk
      type: mozilla-foundation/common_voice_10_0
      config: uk
      split: test
      args: uk
    metrics:
    - name: Wer
      type: wer
      value: 27
---
---

🇺🇦 Join Ukrainian Speech Recognition Community - https://t.me/speech_recognition_uk

⭐ See other Ukrainian models - https://github.com/egorsmkv/speech-recognition-uk

Code for fine-tuning: https://github.com/egorsmkv/whisper-ukrainian

Tests:

- WER: 27% (model quality is 73%)

The test with the original Whisper model is WER 30.57% (model quality is 69.43%)

Tests were with https://github.com/egorsmkv/cv10-uk-testset-clean
