---
language:
- be
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small Belarusian
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 be
      type: mozilla-foundation/common_voice_11_0
      config: be
      split: validation
      args: be
    metrics:
    - type: wer
      name: WER
      value: 6.3671568743912

  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 be
      type: mozilla-foundation/common_voice_11_0
      config: be
      split: test
      args: be
    metrics:
    - type: wer
      name: WER
      value: 6.79

  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: google/fleurs
      type: google/fleurs
      config: be_by
      split: test
    metrics:
    - type: wer
      value: 43.615168811067036
      name: "WER (reference column: transcription)"
    - type: wer
      value: 45.89674723962996
      name: "WER (reference column: raw_transcription)"
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Belarusian

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the mozilla-foundation/common_voice_11_0 be dataset.
It achieves the following results on the evaluation set:
- Loss on validation: 0.0706
- WER on validation set: 6.3672
- WER on test set: 6.79

## Source code
All the source coude is located both in:
* [GitHub repository](https://github.com/yks72p/whisper-finetuning-be)
* and under `src` folder

Code in these 2 places should be the same. GitHub is used to make development and training of multiple models (small, base, etc.) easier.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 12000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer     |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|
| 0.1907        | 0.08  | 1000  | 0.2546          | 25.4639 |
| 0.1482        | 0.17  | 2000  | 0.1641          | 17.1676 |
| 0.1175        | 0.25  | 3000  | 0.1454          | 15.5940 |
| 0.0958        | 0.33  | 4000  | 0.1261          | 13.2625 |
| 0.099         | 0.42  | 5000  | 0.1012          | 10.6143 |
| 0.028         | 1.05  | 6000  | 0.1053          | 9.8794  |
| 0.0473        | 1.13  | 7000  | 0.1029          | 10.3078 |
| 0.0391        | 1.21  | 8000  | 0.0924          | 9.2419  |
| 0.0423        | 1.3   | 9000  | 0.0797          | 7.9249  |
| 0.0604        | 1.38  | 10000 | 0.0688          | 7.0150  |
| 0.0121        | 2.01  | 11000 | 0.0696          | 6.4638  |
| 0.0155        | 2.1   | 12000 | 0.0706          | 6.3672  |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
