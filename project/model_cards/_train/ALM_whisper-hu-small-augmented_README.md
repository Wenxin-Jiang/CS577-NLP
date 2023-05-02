---
language:
- hu
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small Hungarian - Robust
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 hu
      type: mozilla-foundation/common_voice_11_0
      config: hu
      split: test
      args: hu
    metrics:
    - type: wer
      value: 30.904239549362583
      name: Wer
    - type: wer
      value: 26.15
      name: WER
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: google/fleurs
      type: google/fleurs
      config: hu_hu
      split: test
    metrics:
    - type: wer
      value: 35.49
      name: WER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Hungarian - Robust

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the mozilla-foundation/common_voice_11_0 hu dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5243
- Wer: 30.9042

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 128
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.0763        | 7.46  | 500  | 0.5268          | 40.5099 |
| 0.0147        | 14.93 | 1000 | 0.5233          | 36.1429 |
| 0.0064        | 22.39 | 1500 | 0.5467          | 35.0934 |
| 0.0045        | 29.85 | 2000 | 0.5434          | 34.2929 |
| 0.0019        | 37.31 | 2500 | 0.5348          | 32.7868 |
| 0.0008        | 44.78 | 3000 | 0.5314          | 32.0605 |
| 0.0008        | 52.24 | 3500 | 0.5438          | 32.6920 |
| 0.0005        | 59.7  | 4000 | 0.5428          | 32.0931 |
| 0.0003        | 67.16 | 4500 | 0.5328          | 31.2511 |
| 0.0004        | 74.63 | 5000 | 0.5292          | 31.1236 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
