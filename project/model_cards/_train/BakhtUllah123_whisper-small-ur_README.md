---
language:
- ur
license: apache-2.0
tags:
- hf-asr-leaderboard
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_7_0
metrics:
- wer
model-index:
- name: Whisper Small Ur - Bakht Ullah
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 7.0
      type: mozilla-foundation/common_voice_7_0
      args: 'config: ur, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 47.34088927637315
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Ur - Bakht Ullah

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Common Voice 7.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8930
- Wer: 47.3409

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
- lr_scheduler_warmup_steps: 100
- training_steps: 300
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer      |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.6104        | 4.17  | 100  | 1.1037          | 163.3827 |
| 0.0242        | 8.33  | 200  | 0.8656          | 47.6024  |
| 0.0042        | 12.5  | 300  | 0.8930          | 47.3409  |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.2
