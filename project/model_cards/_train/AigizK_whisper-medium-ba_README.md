---
license: apache-2.0
tags:
- generated_from_trainer
- whisper-event
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: openai/whisper-medium
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: common_voice_11_0
      type: common_voice_11_0
      config: ba
      split: test
      args: ba
    metrics:
    - name: Wer
      type: wer
      value: 19.56338265908963
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# openai/whisper-small

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the common_voice_11_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2195
- Wer: 19.56

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
- train_batch_size: 2
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 10000
- mixed_precision_training: Native AMP

### Training results

| Epoch | Step | Wer     |
|:-------------:|:-----:|:----:|
| 0.1   | 1000 | 43.61 |
| 0.2   | 2000 | 36.79 |
| 0.3   | 3000 | 33.05 |
| 0.4   | 4000 | 29.53 |
| 0.5   | 5000 | 26.01 |
| 0.6   | 6000 | 23.44 |
| 0.7   | 7000 | 22.22 |
| 0.8   | 8000 | 21.88 |
| 0.9   | 9000 | 20.53 |
| 1.0   | 10000 | 19.56 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2