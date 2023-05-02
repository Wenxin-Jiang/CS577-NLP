---
language:
- hi
license: apache-2.0
tags:
- hf-asr-leaderboard
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small Fr - Joss
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11.0 FR
      type: mozilla-foundation/common_voice_11_0
      args: 'config: fr, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 24.03653329331678
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Fr - Joss

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Common Voice 11.0 FR dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4212
- Wer: 24.0365

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
- lr_scheduler_warmup_steps: 500
- training_steps: 4000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.3803        | 0.99  | 1000 | 0.3992          | 23.9465 |
| 0.2214        | 1.99  | 2000 | 0.3902          | 22.8108 |
| 0.0986        | 2.98  | 3000 | 0.4028          | 22.4459 |
| 0.0478        | 3.98  | 4000 | 0.4212          | 24.0365 |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.2
