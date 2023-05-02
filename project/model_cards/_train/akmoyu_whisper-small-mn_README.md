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
- name: Whisper Small Mn - akmoyu
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
      value: 50.51878549584971
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Mn - akmoyu

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8308
- Wer: 50.5188

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
| 0.0306        | 7.94  | 1000 | 0.6344          | 52.8724 |
| 0.0017        | 15.87 | 2000 | 0.7480          | 50.3659 |
| 0.0004        | 23.81 | 3000 | 0.8137          | 50.5406 |
| 0.0003        | 15.87 | 4000 | 0.8308          | 50.5188 |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.6.1
- Tokenizers 0.13.2
