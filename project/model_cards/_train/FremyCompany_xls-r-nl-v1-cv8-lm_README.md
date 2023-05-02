---
language:
- nl
tags:
- automatic-speech-recognition
- hf-asr-leaderboard
- model_for_talk
- mozilla-foundation/common_voice_8_0
- nl
- robust-speech-event
- vl
datasets:
- mozilla-foundation/common_voice_8_0
- multilingual_librispeech
model-index:
- name: xls-r-nl-v1-cv8-lm
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: nl
    metrics:
    - name: Test WER
      type: wer
      value: 6.69
    - name: Test CER
      type: cer
      value: 1.97
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
      value: 20.79
    - name: Test CER
      type: cer
      value: 10.72
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
      value: 19.71
---

# XLS-R-based CTC model with 5-gram language model from Common Voice

This model is a version of [facebook/wav2vec2-xls-r-2b-22-to-16](https://huggingface.co/facebook/wav2vec2-xls-r-2b-22-to-16) fine-tuned mainly on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - NL dataset (see details below), on which a small 5-gram language model is added based on the Common Voice training corpus. This model achieves the following results on the evaluation set (of Common Voice 8.0):
- Wer: 0.0669
- Cer: 0.0197

## Model description

The model takes 16kHz sound input, and uses a Wav2Vec2ForCTC decoder with 48 letters to output the final result. 

To improve accuracy, a beam decoder is used; the beams are scored based on 5-gram language model trained on the Common Voice 8 corpus.

## Intended uses & limitations

This model can be used to transcribe Dutch or Flemish spoken dutch to text (without punctuation).

## Training and evaluation data

0. The model was initialized with [the 2B parameter model from Facebook](facebook/wav2vec2-xls-r-2b-22-to-16).
1. The model was then trained `2000` iterations (batch size 32) on [the `dutch` configuration of the `multilingual_librispeech` dataset](https://huggingface.co/datasets/multilingual_librispeech/).
1. The model was then trained `2000` iterations (batch size 32) on [the `nl` configuration of the `common_voice_8_0` dataset](https://huggingface.co/datasets/mozilla-foundation/common_voice_8_0).
2. The model was then trained `6000` iterations (batch size 32) on [the `cgn` dataset](https://taalmaterialen.ivdnt.org/download/tstc-corpus-gesproken-nederlands/).
3. The model was then trained `6000` iterations (batch size 32) on [the `nl` configuation of the `common_voice_8_0` dataset](https://huggingface.co/datasets/mozilla-foundation/common_voice_8_0).

### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0
