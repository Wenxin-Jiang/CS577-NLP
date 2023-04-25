---
language: te
metrics:
- wer
tags:
- audio
- automatic-speech-recognition
- speech
- xlsr-fine-tuning
license: apache-2.0
model-index:
- name: Henil Panchal Facebook XLSR Wav2Vec2 Large 53 Telugu
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    metrics:
       - name: Test WER
         type: wer
         value: 41.90
---
# Wav2Vec2-Large-XLSR-53-Telugu

Fine-tuned [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on Telugu using the ASR IIIT-H dataset.
When using this model, make sure that your speech input is sampled at 16kHz.

**Test Result**: 41.90%
## Training
70% of the O part of ASR IIIT-H Telugu dataset was used for training.
