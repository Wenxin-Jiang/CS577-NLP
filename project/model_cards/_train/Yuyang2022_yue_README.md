---
language:
- yue
license: apache-2.0
tags:
- hf-asr-leaderboard
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11
metrics:
- wer
model-index:
- name: Whisper Base Yue
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11.0 yue
      type: mozilla-foundation/common_voice_11
      config: unclear
      split: None
      args: 'config: yue, split: train'
    metrics:
    - name: Wer
      type: wer
      value: 69.58637469586375
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Base Yue

This model is a fine-tuned version of [openai/whisper-base](https://huggingface.co/openai/whisper-base) on the Common Voice 11.0 yue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3671
- Wer: 69.5864

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 200
- training_steps: 1000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.0998        | 2.78  | 500  | 0.3500          | 71.4517 |
| 0.0085        | 5.56  | 1000 | 0.3671          | 69.5864 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
