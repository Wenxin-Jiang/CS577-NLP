---
language: pa
#datasets:
#- Interspeech 2021
metrics:
- wer
tags:
- audio
- automatic-speech-recognition
- speech
license: mit
model-index:
- name: Wav2Vec2 Vakyansh Punjabi Model by Harveen Chadha
  results:
  - task:
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice hi
      type: common_voice
      args: pa
    metrics:
    - name: Test WER
      type: wer
      value: 33.17
---

Fine-tuned on Multilingual Pretrained Model [CLSRIL-23](https://arxiv.org/abs/2107.07402). The original fairseq checkpoint is present [here](https://github.com/Open-Speech-EkStep/vakyansh-models). When using this model, make sure that your speech input is sampled at 16kHz.
**Note: The result from this model is without a language model so you may witness a higher WER in some cases.**
