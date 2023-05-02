---
language:
- da
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Medium Danish
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0
      type: mozilla-foundation/common_voice_11_0
      config: da
      split: test
      args: da
    metrics:
    - name: Wer
      type: wer
      value: 15.36559705418201
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium Danish

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the mozilla-foundation/common_voice_11_0 da dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5759
- Wer: 15.3656

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-06
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.016         | 7.58  | 1000 | 0.4492          | 15.7391 |
| 0.0014        | 15.15 | 2000 | 0.5306          | 15.4550 |
| 0.0004        | 22.73 | 3000 | 0.5759          | 15.3656 |
| 0.0003        | 30.3  | 4000 | 0.5981          | 15.4655 |
| 0.0002        | 37.88 | 5000 | 0.6072          | 15.5076 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
