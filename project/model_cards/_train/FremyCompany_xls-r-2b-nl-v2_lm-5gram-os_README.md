---
language:
- nl
tags:
- automatic-speech-recognition
- hf-asr-leaderboard
- model_for_talk
- mozilla-foundation/common_voice_8_0
- nl
- nl_BE
- nl_NL
- robust-speech-event
datasets:
- mozilla-foundation/common_voice_8_0
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
      value: 4.06
    - name: Test CER
      type: cer
      value: 1.22
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
      value: 17.77
    - name: Test CER
      type: cer
      value: 9.77
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
      value: 16.32
---

# XLS-R-based CTC model with 5-gram language model from Open Subtitles

This model is a version of [facebook/wav2vec2-xls-r-2b-22-to-16](https://huggingface.co/facebook/wav2vec2-xls-r-2b-22-to-16) fine-tuned mainly on the [CGN dataset](https://taalmaterialen.ivdnt.org/download/tstc-corpus-gesproken-nederlands/), as well as the [MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - NL](https://commonvoice.mozilla.org) dataset (see details below), on which a large 5-gram language model is added based on the Open Subtitles Dutch corpus. This model achieves the following results on the evaluation set (of Common Voice 8.0):
- Wer: 0.04057
- Cer: 0.01222

## Model description

The model takes 16kHz sound input, and uses a Wav2Vec2ForCTC decoder with 48 letters to output the letter-transcription probabilities per frame. 

To improve accuracy, a beam-search decoder based on `pyctcdecode` is then used; it reranks the most promising alignments based on a 5-gram language model trained on the Open Subtitles Dutch corpus.

## Intended uses & limitations

This model can be used to transcribe Dutch or Flemish spoken dutch to text (without punctuation).

## Training and evaluation data

The model was:

0. initialized with [the 2B parameter model from Facebook](facebook/wav2vec2-xls-r-2b-22-to-16).
1. trained `5` epochs (6000 iterations of batch size 32) on [the `cv8/nl` dataset](https://huggingface.co/datasets/mozilla-foundation/common_voice_8_0).
2. trained `1` epoch (36000 iterations of batch size 32) on [the `cgn` dataset](https://taalmaterialen.ivdnt.org/download/tstc-corpus-gesproken-nederlands/).
3. trained `5` epochs (6000 iterations of batch size 32) on [the `cv8/nl` dataset](https://huggingface.co/datasets/mozilla-foundation/common_voice_8_0).

### Framework versions

- Transformers 4.16.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0