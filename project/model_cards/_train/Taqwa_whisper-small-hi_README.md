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
- name: Whisper Small Hi - Sanchit Gandhi
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
      value: 35.74028612545501
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Hi - Sanchit Gandhi

This model is a fine-tuned version of [Taqwa/whisper-small-hiTaqwa](https://huggingface.co/Taqwa/whisper-small-hiTaqwa) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3353
- Wer: 35.7403

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
- training_steps: 500
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.0762        | 0.31  | 125  | 0.2818          | 33.3573 |
| 0.0653        | 0.61  | 250  | 0.2930          | 33.9584 |
| 0.062         | 0.92  | 375  | 0.3060          | 34.7456 |
| 0.0518        | 1.22  | 500  | 0.3353          | 35.7403 |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
