---
language:
- id
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
model-index:
- name: Whisper Medium ID - FLEURS-CV
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: google/fleurs
      type: google/fleurs
      config: id_id
      split: test
    metrics:
    - type: wer
      value: 7.8
      name: WER
    - type: cer
      value: 2.43
      name: CER
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0
      type: mozilla-foundation/common_voice_11_0
      config: id
      split: test
    metrics:
    - type: wer
      value: 8.67
      name: WER
    - type: cer
      value: 2.71
      name: CER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium ID - FLEURS-CV

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the None dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.2563
- eval_wer: 8.4690
- eval_runtime: 2961.9108
- eval_samples_per_second: 1.453
- eval_steps_per_second: 0.091
- epoch: 14.29
- step: 5000

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
- training_steps: 10000
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
