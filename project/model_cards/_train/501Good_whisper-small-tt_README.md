---
language:
- tt
license: apache-2.0
tags:
- whisper-event
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small Tatar - Kirill Milintsevich
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 tt
      type: mozilla-foundation/common_voice_11_0
      config: tt
      split: test
      args: tt
    metrics:
    - name: Wer
      type: wer
      value: 29.091166477916197
---

# Whisper Small Tatar - Kirill Milintsevich

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4745
- Wer: 29.1407

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
- train_batch_size: 64
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
| 0.0415        | 4.98  | 1000 | 0.3252          | 29.9512 |
| 0.0041        | 9.95  | 2000 | 0.3982          | 29.4805 |
| 0.0007        | 14.93 | 3000 | 0.4457          | 29.1513 |
| 0.0003        | 19.9  | 4000 | 0.4665          | 29.0912 |
| 0.0002        | 24.88 | 5000 | 0.4745          | 29.1407 |