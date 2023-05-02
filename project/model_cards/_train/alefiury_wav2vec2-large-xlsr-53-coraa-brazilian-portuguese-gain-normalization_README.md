---
language: pt
datasets:
- CORAA
- common_voice 
- mls
- cetuc
- voxforge
metrics:
- wer
tags:
- audio
- speech
- wav2vec2
- pt
- portuguese-speech-corpus
- automatic-speech-recognition
- speech
- PyTorch
license: apache-2.0
model-index:
- name: Alef Iury XLSR Wav2Vec2 Large 53 Portuguese
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    metrics:
       - name: Test CORAA WER
         type: wer
         value: 24.89%
---

# Wav2vec 2.0 trained with CORAA Portuguese Dataset and Open Portuguese Datasets

This a the demonstration of a fine-tuned Wav2vec model for Portuguese using the following  datasets:

- [CORAA dataset](https://github.com/nilc-nlp/CORAA)
- [CETUC](http://www02.smt.ufrj.br/~igor.quintanilha/alcaim.tar.gz).
- [Multilingual Librispeech (MLS)](http://www.openslr.org/94/).
- [VoxForge](http://www.voxforge.org/).
- [Common Voice 6.1](https://commonvoice.mozilla.org/pt).

## Repository

The repository that implements the model to be trained and tested is avaible [here](https://github.com/alefiury/SE-R_2022_Challenge_Wav2vec2).