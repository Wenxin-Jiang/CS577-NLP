---
language:
- el
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
- hf-asr-leaderboard
datasets:
- common_voice_11_0
metrics:
- wer
model-index:
- name: whisper-large-el
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0
      type: mozilla-foundation/common_voice_11_0
      config: el
      split: test
      args: el
    metrics:
    - name: Wer
      type: wer
      value: 8.998885586924219
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-large-el

This model is a fine-tuned version of [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) on the mozilla-foundation/common_voice_11_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1895
- Wer: 8.9989

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
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.0987        | 0.2   | 1000 | 0.1966          | 13.6516 |
| 0.0772        | 0.4   | 2000 | 0.1812          | 12.2771 |
| 0.0398        | 0.6   | 3000 | 0.1734          | 11.3113 |
| 0.0775        | 0.8   | 4000 | 0.1699          | 9.7975  |
| 0.0314        | 1.0   | 5000 | 0.1895          | 8.9989  |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
