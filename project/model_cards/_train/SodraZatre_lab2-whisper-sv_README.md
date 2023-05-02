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
- name: Whisper Small Hi - Swedish
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11.0
      type: mozilla-foundation/common_voice_11_0
      config: config.json
      split: None
      args: 'config: hi, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 19.894598155467722
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Hi - Swedish

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3260
- Wer: 19.8946

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
| 0.3144        | 0.65  | 500  | 0.3244          | 24.0623 |
| 0.1321        | 1.29  | 1000 | 0.2977          | 21.5563 |
| 0.1318        | 1.94  | 1500 | 0.2788          | 20.9190 |
| 0.052         | 2.59  | 2000 | 0.2852          | 20.3329 |
| 0.0203        | 3.23  | 2500 | 0.3017          | 19.8677 |
| 0.0174        | 3.88  | 3000 | 0.3008          | 19.9941 |
| 0.0083        | 4.53  | 3500 | 0.3216          | 20.0022 |
| 0.0039        | 5.17  | 4000 | 0.3260          | 19.8946 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
