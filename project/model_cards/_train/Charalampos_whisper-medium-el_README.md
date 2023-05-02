---
language:
- el
license: apache-2.0
tags:
- generated_from_trainer
- hf-asr-leaderboard
- whisper-event
datasets:
- common_voice_11_0
metrics:
- wer
model-index:
- name: openai/whisper-medium
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0
      type: mozilla-foundation/common_voice_11_0
      config: el
      split: test
      args: el
    metrics:
    - type: wer
      value: 11.469167904903417
      name: Wer
    - type: wer
      value: 11.43
      name: WER
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: google/fleurs
      type: google/fleurs
      config: el_gr
      split: test
    metrics:
    - type: wer
      value: 8.99
      name: WER
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: Charalampos/greek_data
      type: Charalampos/greek_data
      config: el
      split: train
    metrics:
    - type: wer
      value: 21.33
      name: WER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# openai/whisper-medium

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the common_voice_11_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3367
- Wer: 11.4692

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.0108        | 4.04  | 1000 | 0.2423          | 12.7600 |
| 0.0013        | 9.04  | 2000 | 0.2810          | 11.9799 |
| 0.0001        | 14.04 | 3000 | 0.3152          | 11.5435 |
| 0.0001        | 19.04 | 4000 | 0.3304          | 11.4320 |
| 0.0001        | 24.04 | 5000 | 0.3367          | 11.4692 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
