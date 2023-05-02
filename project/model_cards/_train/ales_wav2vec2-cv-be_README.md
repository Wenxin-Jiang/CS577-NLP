---
license: gpl-3.0

language:
- be

tags:
- audio
- speech
- automatic-speech-recognition

datasets:
- mozilla-foundation/common_voice_8_0

metrics:
- wer

model-index:
- name: wav2vec2
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: be
    metrics:
    - name: Dev WER
      type: wer
      value: 17.61
    - name: Test WER
      type: wer
      value: 18.7
    - name: Dev WER (with LM)
      type: wer
      value: 11.5
    - name: Test WER (with LM)
      type: wer
      value: 12.4
---

# Automatic Speech Recognition for Belarusian language

Fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on `mozilla-foundation/common_voice_8_0 be` dataset.

`Train`, `Dev`, `Test` splits were used as they are present in the dataset. No additional data was used from `Validated` split, 
only 1 voicing of each sentence was used - the way the data was split by [CommonVoice CorporaCreator](https://github.com/common-voice/CorporaCreator). 
To build a better model **one can use additional voicings from `Validated` split** for sentences already present in `Train`, `Dev`, `Test` splits,
i.e. enlarge mentioned splits.

Language model was built using [KenLM](https://kheafield.com/code/kenlm/estimation/). 
5-gram Language model was built on sentences from `Train + (Other - Dev - Test)` splits of `mozilla-foundation/common_voice_8_0 be` dataset.

Source code is available [here](https://github.com/yks72p/stt_be).

## Run model in a browser

This page contains interactive demo widget that lets you test this model right in a browser.

However, this widget uses Acoustic model only **without** Language model that significantly improves overall performance.

You can play with **full pipeline of Acoustic model + Language model** on the following [spaces page](https://huggingface.co/spaces/ales/wav2vec2-cv-be-lm)
(also works from browser).
