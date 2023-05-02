---
language:
- fr
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- robust-speech-event
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: xls-r-300m-fr
  results:
  - task:
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8.0 fr
      type: mozilla-foundation/common_voice_8_0
      args: fr
    metrics:
    - name: Test WER
      type: wer
      value: 36.81
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: fr
    metrics:
    - name: Test WER
      type: wer
      value: 35.55
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: fr
    metrics:
    - name: Test WER
      type: wer
      value: 39.94
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - FR dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2388
- Wer: 0.3681

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1500
- num_epochs: 2.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 4.3748        | 0.07  | 500   | 3.8784          | 1.0    |
| 2.8068        | 0.14  | 1000  | 2.8289          | 0.9826 |
| 1.6698        | 0.22  | 1500  | 0.8811          | 0.7127 |
| 1.3488        | 0.29  | 2000  | 0.5166          | 0.5369 |
| 1.2239        | 0.36  | 2500  | 0.4105          | 0.4741 |
| 1.1537        | 0.43  | 3000  | 0.3585          | 0.4448 |
| 1.1184        | 0.51  | 3500  | 0.3336          | 0.4292 |
| 1.0968        | 0.58  | 4000  | 0.3195          | 0.4180 |
| 1.0737        | 0.65  | 4500  | 0.3075          | 0.4141 |
| 1.0677        | 0.72  | 5000  | 0.3015          | 0.4089 |
| 1.0462        | 0.8   | 5500  | 0.2971          | 0.4077 |
| 1.0392        | 0.87  | 6000  | 0.2870          | 0.3997 |
| 1.0178        | 0.94  | 6500  | 0.2805          | 0.3963 |
| 0.992         | 1.01  | 7000  | 0.2748          | 0.3935 |
| 1.0197        | 1.09  | 7500  | 0.2691          | 0.3884 |
| 1.0056        | 1.16  | 8000  | 0.2682          | 0.3889 |
| 0.9826        | 1.23  | 8500  | 0.2647          | 0.3868 |
| 0.9815        | 1.3   | 9000  | 0.2603          | 0.3832 |
| 0.9717        | 1.37  | 9500  | 0.2561          | 0.3807 |
| 0.9605        | 1.45  | 10000 | 0.2523          | 0.3783 |
| 0.96          | 1.52  | 10500 | 0.2494          | 0.3788 |
| 0.9442        | 1.59  | 11000 | 0.2478          | 0.3760 |
| 0.9564        | 1.66  | 11500 | 0.2454          | 0.3733 |
| 0.9436        | 1.74  | 12000 | 0.2439          | 0.3747 |
| 0.938         | 1.81  | 12500 | 0.2411          | 0.3716 |
| 0.9353        | 1.88  | 13000 | 0.2397          | 0.3698 |
| 0.9271        | 1.95  | 13500 | 0.2388          | 0.3681 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0
