---
language:
- el
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small Greek - Robust
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 el
      type: mozilla-foundation/common_voice_11_0
      config: el
      split: test
      args: el
    metrics:
    - type: wer
      value: 24.52637444279346
      name: Wer
    - type: wer
      value: 20.42
      name: WER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Greek - Robust

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the mozilla-foundation/common_voice_11_0 el dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3605
- Wer: 24.5264

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.2223        | 2.35  | 500  | 0.4403          | 37.9922 |
| 0.0908        | 4.69  | 1000 | 0.4041          | 35.6519 |
| 0.0465        | 7.04  | 1500 | 0.4189          | 34.3053 |
| 0.0168        | 9.39  | 2000 | 0.3972          | 29.9127 |
| 0.0118        | 11.74 | 2500 | 0.4043          | 28.9933 |
| 0.0053        | 14.08 | 3000 | 0.3968          | 28.5940 |
| 0.0032        | 16.43 | 3500 | 0.3664          | 25.6779 |
| 0.0009        | 18.78 | 4000 | 0.3665          | 26.2444 |
| 0.0003        | 21.13 | 4500 | 0.3620          | 25.2879 |
| 0.0004        | 23.47 | 5000 | 0.3570          | 24.8607 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.7.1
- Tokenizers 0.13.2
