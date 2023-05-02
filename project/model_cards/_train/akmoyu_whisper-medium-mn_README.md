---
language:
- mn
license: apache-2.0
tags:
- hf-asr-leaderboard
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Medium Mn - akmoyu
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11.0
      type: mozilla-foundation/common_voice_11_0
      args: 'config: hi, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 42.52948885976409
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium Mn - akmoyu

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7233
- Wer: 42.5295

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
- training_steps: 4000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.0182        | 7.94  | 1000 | 0.5995          | 46.5269 |
| 0.0027        | 15.87 | 2000 | 0.6499          | 44.2169 |
| 0.0002        | 23.81 | 3000 | 0.7057          | 42.5623 |
| 0.0001        | 31.75 | 4000 | 0.7233          | 42.5295 |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.6.1
- Tokenizers 0.13.2
