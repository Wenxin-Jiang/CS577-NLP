---
language:
- uk
library_name: nemo
datasets:
- mozilla-foundation/common_voice_10_0
- Yehor/voa-uk-transcriptions
tags:
- automatic-speech-recognition
model-index:
- name: stt_uk_squeezeformer_rnnt_xs
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Mozilla Common Voice 10.0
      type: mozilla-foundation/common_voice_10_0
      config: clean
      split: test
      args:
        language: uk
    metrics:
    - name: Test WER
      type: wer
      value: 8.814
license: bsd-3-clause
---
# Squeezeformer-RNNT XS (uk-UA)

<style>
img {
 display: inline;
}
</style>

| [![Model architecture](https://img.shields.io/badge/Model_Arch-Squeezeformer--RNNT-lightgrey#model-badge)](#model-architecture)
| [![Model size](https://img.shields.io/badge/Params-10M-lightgrey#model-badge)](#model-architecture)
| [![Language](https://img.shields.io/badge/Language-uk--UA-lightgrey#model-badge)](#datasets) |