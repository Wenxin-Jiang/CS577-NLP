---
language:
- lt
license: apache-2.0
tags:
- hf-asr-leaderboard
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small lt - Lithuanian
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11.0
      type: mozilla-foundation/common_voice_11_0
      config: None
      split: None
      args: 'config: lt, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 32.49711764004294
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small lt - Lithuanian

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3840
- Wer: 32.4971

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 250
- training_steps: 4000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.3788        | 0.9   | 500  | 0.4432          | 45.1716 |
| 0.2087        | 1.8   | 1000 | 0.3671          | 37.6456 |
| 0.0961        | 2.7   | 1500 | 0.3548          | 35.5703 |
| 0.0479        | 3.6   | 2000 | 0.3609          | 34.1709 |
| 0.0157        | 4.5   | 2500 | 0.3665          | 33.3400 |
| 0.0089        | 5.4   | 3000 | 0.3775          | 32.7754 |
| 0.0038        | 6.29  | 3500 | 0.3826          | 32.5607 |
| 0.0033        | 7.19  | 4000 | 0.3840          | 32.4971 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
