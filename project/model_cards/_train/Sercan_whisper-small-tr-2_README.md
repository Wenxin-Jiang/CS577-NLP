---
language:
- tr
license: apache-2.0
tags:
- whisper
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small Turkish
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 tr
      type: mozilla-foundation/common_voice_11_0
      config: tr
      split: test
      args: tr
    metrics:
    - name: Wer
      type: wer
      value: 16.632698616044568
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Turkish

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the mozilla-foundation/common_voice_11_0 tr dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2576
- Wer: 16.6327
- Cer: 4.2853

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
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|
| 0.1412        | 0.08  | 400  | 0.2656          | 19.8335 | 5.2393 |
| 0.0851        | 1.03  | 800  | 0.2382          | 18.6300 | 4.8916 |
| 0.0525        | 1.11  | 1200 | 0.2532          | 19.1696 | 5.2238 |
| 0.0163        | 2.07  | 1600 | 0.2447          | 17.2014 | 4.5840 |
| 0.0202        | 3.02  | 2000 | 0.2472          | 17.1063 | 4.4935 |
| 0.0075        | 3.1   | 2400 | 0.2503          | 17.0151 | 4.4318 |
| 0.0039        | 4.05  | 2800 | 0.2514          | 16.7433 | 4.3655 |
| 0.0038        | 5.01  | 3200 | 0.2565          | 16.8870 | 4.3582 |
| 0.0023        | 5.09  | 3600 | 0.2590          | 16.6987 | 4.3337 |
| 0.0013        | 6.04  | 4000 | 0.2576          | 16.6327 | 4.2853 |
| 0.0011        | 6.12  | 4400 | 0.2647          | 16.9122 | 4.3556 |
| 0.001         | 7.07  | 4800 | 0.2615          | 16.6346 | 4.2839 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.8.1.dev0
- Tokenizers 0.13.2
