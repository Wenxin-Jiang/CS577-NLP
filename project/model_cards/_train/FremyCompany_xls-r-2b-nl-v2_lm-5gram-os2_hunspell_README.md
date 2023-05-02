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
      value: 3.93
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
      value: 16.35
    - name: Test CER
      type: cer
      value: 9.64
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
      value: 15.81
---

# XLS-R-based CTC model with 5-gram language model from Open Subtitles

This model is a version of [facebook/wav2vec2-xls-r-2b-22-to-16](https://huggingface.co/facebook/wav2vec2-xls-r-2b-22-to-16) fine-tuned mainly on the [CGN dataset](https://taalmaterialen.ivdnt.org/download/tstc-corpus-gesproken-nederlands/), as well as the [MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - NL](https://commonvoice.mozilla.org) dataset (see details below), on which a large 5-gram language model is added based on the Open Subtitles Dutch corpus. This model achieves the following results on the evaluation set (of Common Voice 8.0):
- Wer: 0.03931
- Cer: 0.01224

> **IMPORTANT NOTE**: The `hunspell` typo fixer is **not enabled** on the website, which returns raw CTC+LM results. Hunspell reranking is only available in the `eval.py` decoding script. For best results, please use the code in that file while using the model locally for inference.

> **IMPORTANT NOTE**: Evaluating this model requires `apt install libhunspell-dev` and a pip install of `hunspell` in addition to pip installs of `pipy-kenlm` and `pyctcdecode` (see `install_requirements.sh`); in addition, the chunking lengths and strides were optimized for the model as `12s` and `2s` respectively (see `eval.sh`).

> **QUICK REMARK**: The "Robust Speech Event" set does not contain cleaned transcription text, so its WER/CER are vastly over-estimated. For instance `2014` in the dev set is left as a number but will be recognized as `tweeduizend veertien`, which counts as 3 mistakes (`2014` missing, and both `tweeduizend` and `veertien` wrongly inserted). Other normalization problems in the dev set include the presence of single quotes around some words, that then end up as non-match despite being the correct word (but without quotes), and the removal of some speech words in the final transcript (`ja`, etc...). As a result, our real error rate on the dev set is significantly lower than reported.
>
> ![Image showing the difference between the prediction and target of the dev set](https://huggingface.co/FremyCompany/xls-r-2b-nl-v2_lm-5gram-os2_hunspell/resolve/main/dev_set_diff_4.png)
>
> You can compare the [predictions](https://huggingface.co/FremyCompany/xls-r-2b-nl-v2_lm-5gram-os2_hunspell/blob/main/log_speech-recognition-community-v2_dev_data_nl_validation_predictions.txt) with the [targets](https://huggingface.co/FremyCompany/xls-r-2b-nl-v2_lm-5gram-os2_hunspell/blob/main/log_speech-recognition-community-v2_dev_data_nl_validation_targets.txt) on the validation dev set yourself, for example using [this diffing tool](https://countwordsfree.com/comparetexts).

> **WE DO SPEECH RECOGNITION**: Hello reader! If you are considering using this (or another) model in production, but would benefit from a model fine-tuned specifically for your use case (using text and/or labelled speech), feel free to [contact our team](https://www.ugent.be/ea/idlab/en/research/semantic-intelligence/speech-and-audio-processing.htm). This model was developped during the [Robust Speech Recognition challenge](https://discuss.huggingface.co/t/open-to-the-community-robust-speech-recognition-challenge/13614) event by [François REMY](https://www.linkedin.com/in/fremycompany/) [(twitter)](https://twitter.com/FremyCompany) and [Geoffroy VANDERREYDT](https://be.linkedin.com/in/geoffroy-vanderreydt-a4421460). 

> We would like to thank [OVH](https://www.ovhcloud.com/en/public-cloud/ai-training/) for providing us with a V100S GPU.

## Model description

The model takes 16kHz sound input, and uses a Wav2Vec2ForCTC decoder with 48 letters to output the letter-transcription probabilities per frame. 

To improve accuracy, a beam-search decoder based on `pyctcdecode` is then used; it reranks the most promising alignments based on a 5-gram language model trained on the Open Subtitles Dutch corpus.

To further deal with typos, `hunspell` is used to propose alternative spellings for words not in the unigrams of the language model. These alternatives are then reranked based on the language model trained above, and a penalty proportional to the levenshtein edit distance between the alternative and the recognized word. This for examples enables to correct `collegas` into `collega's` or `gogol` into `google`.

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