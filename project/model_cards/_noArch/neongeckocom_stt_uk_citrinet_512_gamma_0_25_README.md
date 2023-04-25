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
- name: stt_uk_citrinet_512_gamma_0_25
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
      value: 8.609
license: bsd-3-clause
---
# NVIDIA Streaming Citrinet 512 (uk-UA)

<style>
img {
 display: inline;
}
</style>

| [![Model architecture](https://img.shields.io/badge/Model_Arch-Citrinet--CTC-lightgrey#model-badge)](#model-architecture)
| [![Model size](https://img.shields.io/badge/Params-36M-lightgrey#model-badge)](#model-architecture)
| [![Language](https://img.shields.io/badge/Language-uk--UA-lightgrey#model-badge)](#datasets) |
## Attribution
As initial checkpoint used [stt_en_citrinet_512_gamma_0_25](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/stt_en_citrinet_512_gamma_0_25) by [NVIDIA](https://github.com/NVIDIA) licensed under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)