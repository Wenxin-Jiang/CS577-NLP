---
language:
- ml
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
- name: whisper_malayalam_largev2
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0
      type: mozilla-foundation/common_voice_11_0
      config: ml
      split: test
    metrics:
    - name: Wer
      type: wer
      value: 68.7356
---


<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper-fineTuning-malayalam

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4138
- Wer: 68.7356

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
- train_batch_size: 12
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 4000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.0099        | 1.88  | 1000 | 0.3563          | 69.6552 |
| 0.0046        | 3.77  | 2000 | 0.3860          | 70.1149 |
| 0.001         | 5.65  | 3000 | 0.4105          | 70.3448 |
| 0.0001        | 7.53  | 4000 | 0.4138          | 68.7356 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
