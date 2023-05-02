---
language:
- lt
license: apache-2.0
tags:
- whisper-event
- hf-asr-leaderboard
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Medium Lithuanian
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0
      type: mozilla-foundation/common_voice_11_0
      args: 'config: lt, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 20.446244
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium Lithuanian CV11

This model is a fine-tuned version of [openai/whisper-large](https://huggingface.co/openai/whisper-medium) on the mozilla-foundation/common_voice_11_0 lt dataset.
It achieves the following results on the evaluation set:
- Loss: 0.354951
- Wer: 20.446244

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters



### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.0056        | 9.42  | 1000 | 0.3252          | 20.5534 |
| 0.0023        | 18.8  | 2000 | 0.3549          | 20.4462 |



### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2