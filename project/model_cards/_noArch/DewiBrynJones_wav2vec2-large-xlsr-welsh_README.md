---
language: cy
datasets:
- common_voice 
metrics:
- wer
tags:
- audio
- automatic-speech-recognition
- speech
- xlsr-fine-tuning-week
license: apache-2.0
model-index:
- name: wav2vec2-xlsr-welsh (by Dewi Bryn Jones, fine tuning week - March 2021)
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice cy
      type: common_voice
      args: cy
    metrics:
       - name: Test WER
         type: wer
         value: 25.59%
---

# Wav2Vec2-Large-XLSR-Welsh

This model has moved to https://huggingface.co/techiaith/wav2vec2-xlsr-ft-cy

