---
language:
- da
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small Danish - Robust
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 da
      type: mozilla-foundation/common_voice_11_0
      config: da
      split: test
      args: da
    metrics:
    - type: wer
      value: 32.3250920568122
      name: Wer
    - type: wer
      value: 28.09
      name: WER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Danish - Robust

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the mozilla-foundation/common_voice_11_0 da dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7926
- Wer: 32.3251

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
| 0.0232        | 15.15 | 1000 | 0.7538          | 35.5813 |
| 0.0061        | 30.3  | 2000 | 0.7933          | 34.3766 |
| 0.0016        | 45.45 | 3000 | 0.7993          | 33.5823 |
| 0.0003        | 60.61 | 4000 | 0.7986          | 31.6097 |
| 0.0002        | 75.76 | 5000 | 0.7901          | 32.1357 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.8.0
- Tokenizers 0.13.2
