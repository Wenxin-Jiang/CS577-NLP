---
language:
- nl
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- nl
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-300m-cv8-nl
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
      value: 14.53
    - name: Test CER
      type: cer
      value: 4.7
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
      value: 33.7
    - name: Test CER
      type: cer
      value: 15.64
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
      value: 35.19
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-cv8-nl

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset. In addition a 6gram KenLM model was trained and used. The KenLM model was based on train+validation Common Voice 8
It achieves results depicted on the rigth side on the model card (testset CV8)

## Model description

Dutch wav2vec2-xls-r-300m model using Common Voice 8 dataset

## Intended uses & limitations

More information needed

## Training and evaluation data

The model was trained on Dutch common voice 8 with 75 epochs. The train set consisted of the common voice 8 train set and evaluation set was the common voice 8 validation set. The WER reported is on the common voice 8 test set which was not part of training nor validation (eval)

## Training procedure

### Training hyperparameters

### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.18.1
- Tokenizers 0.11.0
