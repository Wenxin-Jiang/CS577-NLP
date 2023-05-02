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
- name: wav2vec2-large-xls-r-1b-nl-lm
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
      value: 9.73
    - name: Test CER
      type: cer
      value: 2.89
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
      value: 27.27
    - name: Test CER
      type: cer
      value: 13.23
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
      value: 27.67
---
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-1b-nl-lm

This model is a fine-tuned version of [wav2vec2-large-xls-r-1b-nl-lm](https://huggingface.co/facebook/wav2vec2-xls-r-1b) on the common_voice 8 dataset.
It achieves the following results on the test set:
- Loss: 0.1479
- Wer: 0.1156

Note that the above test results come from the original model without LM (language model) which can be found at https://huggingface.co/RuudVelo/wav2vec2-large-xls-r-1b-nl. The results with the LM model can be found on the right side of this model card.

## Model description
Model RuudVelo/wav2vec2-large-xls-r-1b-nl which has been improved with a KenLM 5-gram. 
## Intended uses & limitations
More information needed
## Training and evaluation data
Common Voice 8 nl dataset has been used for the model
## Training procedure

### Training hyperparameters
Parameters can be found in the run.sh file at https://huggingface.co/RuudVelo/wav2vec2-large-xls-r-1b-nl 

### Framework versions
- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0