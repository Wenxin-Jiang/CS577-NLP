---
language:
- gl
license: apache-2.0
tags:
- hf-asr-leaderboard
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: "Whisper Small GL - Santiago Param\xE9s-Est\xE9vez"
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11.0
      type: mozilla-foundation/common_voice_11_0
      config: gl
      split: test
      args: 'config: gl, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 15.233405065386526
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small GL - Santiago Paramés-Estévez

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3179
- Wer: 15.2334

## Model description

This model was fine-tuned using Sanchit Gandhi's notebook: https://huggingface.co/blog/fine-tune-whisper

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 4000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.0707        | 2.69  | 1000 | 0.2596          | 16.4915 |
| 0.0063        | 5.38  | 2000 | 0.2952          | 15.8583 |
| 0.0014        | 8.06  | 3000 | 0.3105          | 15.2624 |
| 0.0011        | 10.75 | 4000 | 0.3179          | 15.2334 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1
- Tokenizers 0.13.2
