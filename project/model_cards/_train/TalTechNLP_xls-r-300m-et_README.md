---
license: cc-by-4.0
tags:
- audio
- automatic-speech-recognition
- hf-asr-leaderboard
language: et
model-index:
- name: xls-r-300m-et
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 
      type: common_voice
      args: et
    metrics:
    - name: Test WER
      type: wer
      value: 12.520395591222402
    - name: Test CER
      type: cer
      value: 2.7091152438624897
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: et
    metrics:
    - name: Test WER
      type: wer
      value: 13.38447882323104
    - name: Test CER
      type: cer
      value: 2.9816686199500255
---


# XLS-R-300m-ET

This is a XLS-R-300M model [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) finetuned on around 800 hours of diverse Estonian data.

## Model description
This is a general-purpose Estonian ASR model trained in the Lab of Language Technology at TalTech. It consists of only the CTC-based end-to-end model, no language model is currently provided.

## Intended uses & limitations

This model is intended for general-purpose speech recognition, such as broadcast conversations, interviews, talks, etc.

## How to use


TODO

#### Limitations and bias

Since this model was trained on mostly broadcast speech and texts from the web, it might have problems correctly decoding the following:
  * Speech containing technical and other domain-specific terms
  * Children's speech
  * Non-native speech
  * Speech recorded under very noisy conditions or with a microphone far from the speaker
  * Very spontaneous and overlapping speech

## Training data
Acoustic training data:

| Type                  | Amount (h) |
|-----------------------|:------:|
| Broadcast speech      |   591  |
| Spontaneous speech    |   53   |
| Elderly speech corpus |   53   |
| Talks, lectures       |   49   |
| Parliament speeches   |   31   |
| *Total*               |   *761*  |


## Training procedure

Finetuned using Fairseq.

## Evaluation results

### WER

|Dataset | WER |
|---|---|
| jutusaated.devset | 7.9 |
| jutusaated.testset | 6.1 |
| Common Voice 6.1 | 12.5 |
| Common Voice 8.0 | 13.4 |
