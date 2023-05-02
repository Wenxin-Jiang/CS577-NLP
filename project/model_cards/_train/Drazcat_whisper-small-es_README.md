---
language:
- es
license: apache-2.0
tags:
- hf-asr-leaderboard
- generated_from_trainer
datasets:
- Drazcat/Cencosud
metrics:
- wer
model-index:
- name: Whisper Small Es - GoCloud
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: 30seg
      type: Drazcat/Cencosud
      args: 'config: es, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 0.0
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Es - GoCloud

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the 30seg dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0028
- Wer: 0.0

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 25
- training_steps: 200
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.2944        | 5.56  | 50   | 0.1392          | 79.6117 |
| 0.08          | 11.11 | 100  | 0.0569          | 46.0472 |
| 0.0204        | 16.67 | 150  | 0.0086          | 0.0     |
| 0.0028        | 22.22 | 200  | 0.0028          | 0.0     |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
