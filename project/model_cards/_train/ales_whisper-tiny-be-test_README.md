---
language:
- be
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Tiny Belarusian
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 be
      type: mozilla-foundation/common_voice_11_0
      config: be
      split: validation
      args: be
    metrics:
    - name: Wer
      type: wer
      value: 46.52014652014652
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Tiny Belarusian

Repo to test model training

This model is a fine-tuned version of [openai/whisper-tiny](https://huggingface.co/openai/whisper-tiny) on the mozilla-foundation/common_voice_11_0 be dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4388
- Wer: 46.5201

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 10
- training_steps: 300
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 2.5366        | 0.05  | 10   | 1.5402          | 94.5055 |
| 1.3721        | 0.1   | 20   | 1.0021          | 75.8242 |
| 0.9921        | 0.15  | 30   | 0.8322          | 75.0916 |
| 0.9844        | 0.2   | 40   | 0.8080          | 72.8938 |
| 0.7071        | 0.25  | 50   | 0.7862          | 77.2894 |
| 0.7998        | 0.3   | 60   | 0.7052          | 68.8645 |
| 0.6935        | 0.35  | 70   | 0.6781          | 64.2857 |
| 0.81          | 0.4   | 80   | 0.6341          | 63.5531 |
| 0.6133        | 0.45  | 90   | 0.6083          | 62.6374 |
| 0.6675        | 0.5   | 100  | 0.5851          | 62.8205 |
| 0.5577        | 0.55  | 110  | 0.5651          | 59.3407 |
| 0.6473        | 0.6   | 120  | 0.5638          | 58.0586 |
| 0.6018        | 0.65  | 130  | 0.5434          | 53.8462 |
| 0.5918        | 0.7   | 140  | 0.5385          | 54.9451 |
| 0.5654        | 0.75  | 150  | 0.5200          | 58.0586 |
| 0.587         | 0.8   | 160  | 0.4974          | 57.1429 |
| 0.6157        | 0.85  | 170  | 0.4834          | 53.2967 |
| 0.6803        | 0.9   | 180  | 0.4852          | 55.8608 |
| 0.4813        | 0.95  | 190  | 0.4686          | 51.2821 |
| 0.4952        | 1.0   | 200  | 0.4624          | 51.4652 |
| 0.3956        | 0.03  | 210  | 0.4690          | 52.0147 |
| 0.3719        | 0.07  | 220  | 0.4673          | 52.7473 |
| 0.3168        | 0.1   | 230  | 0.4499          | 51.4652 |
| 0.3582        | 0.13  | 240  | 0.4525          | 46.8864 |
| 0.2475        | 0.17  | 250  | 0.4612          | 52.3810 |
| 0.2988        | 0.2   | 260  | 0.4346          | 49.8168 |
| 0.2749        | 0.23  | 270  | 0.4249          | 48.9011 |
| 0.3368        | 0.27  | 280  | 0.4388          | 46.5201 |
| 0.2574        | 0.3   | 290  | 0.4309          | 46.7033 |
| 0.2921        | 0.33  | 300  | 0.4282          | 46.7033 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu116
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
