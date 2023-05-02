---
license: apache-2.0
tags:
- generated_from_trainer
- whisper-event
metrics:
- wer
model-index:
- name: whisper-medium-et-ERR2020
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0
      type: mozilla-foundation/common_voice_11_0
      config: et
      split: test
    metrics:
    - type: wer
      value: 20.05
      name: WER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-medium-et-ERR2020

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the following training sets: Common Voice 11, VoxPopuli, FLEURS and [ERR2020](http://bark.phon.ioc.ee/lw/korpused/ERR2020.html). The checkpoint-7000 was on [Whisper Event leaderboard](https://huggingface.co/spaces/whisper-event/winners?dataset=mozilla-foundation%2Fcommon_voice_11_0). Current score is for the final checkpoint. 

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
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 10000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer     |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|
| 0.1828        | 0.1   | 1000  | 0.3547          | 20.8829 |
| 0.09          | 0.2   | 2000  | 0.3476          | 19.0096 |
| 0.083         | 0.3   | 3000  | 0.3386          | 18.1304 |
| 0.0765        | 0.4   | 4000  | 0.3365          | 17.2591 |
| 0.0592        | 0.5   | 5000  | 0.3534          | 19.0213 |
| 0.0672        | 0.6   | 6000  | 0.3622          | 18.4263 |
| 0.0629        | 0.7   | 7000  | 0.3487          | 15.9839 |
| 0.0546        | 1.03  | 8000  | 0.3677          | 16.1021 |
| 0.0459        | 1.13  | 9000  | 0.3704          | 17.9073 |
| 0.0425        | 1.23  | 10000 | 0.3672          | 15.9119 |

The validation set is combined from the validation sets of Common Voice 11, VoxPopuli, FLEURS and ERR2020.

### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.12.1+rocm5.1.1h
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
