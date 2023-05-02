---
language:
- sk
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small Slovak - Robust
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 sk
      type: mozilla-foundation/common_voice_11_0
      config: sk
      split: test
      args: sk
    metrics:
    - type: wer
      value: 43.62208472156116
      name: Wer
    - type: wer
      value: 36.11
      name: WER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Slovak - Robust

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the mozilla-foundation/common_voice_11_0 sk dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7397
- Wer: 43.6221

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
- train_batch_size: 64
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
| 0.0232        | 14.29 | 1000 | 0.7425          | 51.8801 |
| 0.0083        | 28.57 | 2000 | 0.7698          | 48.4888 |
| 0.0006        | 42.86 | 3000 | 0.7640          | 47.5964 |
| 0.0005        | 57.14 | 4000 | 0.7649          | 44.8953 |
| 0.0002        | 71.43 | 5000 | 0.7440          | 44.3598 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.8.0
- Tokenizers 0.13.2
