---
language:
- pt
license: apache-2.0
tags:
- automatic-speech-recognition
- robust-speech-event
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: xls-r-300m-pt
  results:
  - task:
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8.0 pt
      type: mozilla-foundation/common_voice_8_0
      args: pt
    metrics:
    - name: Test WER
      type: wer
      value: 19.361
    - name: Test CER
      type: cer
      value: 5.533
  - task:
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: fr
    metrics:
    - name: Validation WER
      type: wer
      value: 47.812
    - name: Validation CER
      type: cer
      value: 18.805
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8.0
      type: mozilla-foundation/common_voice_8_0
      args: pt
    metrics:
    - name: Test WER
      type: wer
      value: 19.36
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: pt
    metrics:
    - name: Test WER
      type: wer
      value: 48.01
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: pt
    metrics:
    - name: Test WER
      type: wer
      value: 49.21
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - PT dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2290
- Wer: 0.2382

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1500
- num_epochs: 15.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 3.0952        | 0.64  | 500   | 3.0982          | 1.0    |
| 1.7975        | 1.29  | 1000  | 0.7887          | 0.5651 |
| 1.4138        | 1.93  | 1500  | 0.5238          | 0.4389 |
| 1.344         | 2.57  | 2000  | 0.4775          | 0.4318 |
| 1.2737        | 3.21  | 2500  | 0.4648          | 0.4075 |
| 1.2554        | 3.86  | 3000  | 0.4069          | 0.3678 |
| 1.1996        | 4.5   | 3500  | 0.3914          | 0.3668 |
| 1.1427        | 5.14  | 4000  | 0.3694          | 0.3572 |
| 1.1372        | 5.78  | 4500  | 0.3568          | 0.3501 |
| 1.0831        | 6.43  | 5000  | 0.3331          | 0.3253 |
| 1.1074        | 7.07  | 5500  | 0.3332          | 0.3352 |
| 1.0536        | 7.71  | 6000  | 0.3131          | 0.3152 |
| 1.0248        | 8.35  | 6500  | 0.3024          | 0.3023 |
| 1.0075        | 9.0   | 7000  | 0.2948          | 0.3028 |
| 0.979         | 9.64  | 7500  | 0.2796          | 0.2853 |
| 0.9594        | 10.28 | 8000  | 0.2719          | 0.2789 |
| 0.9172        | 10.93 | 8500  | 0.2620          | 0.2695 |
| 0.9047        | 11.57 | 9000  | 0.2537          | 0.2596 |
| 0.8777        | 12.21 | 9500  | 0.2438          | 0.2525 |
| 0.8629        | 12.85 | 10000 | 0.2409          | 0.2493 |
| 0.8575        | 13.5  | 10500 | 0.2366          | 0.2440 |
| 0.8361        | 14.14 | 11000 | 0.2317          | 0.2385 |
| 0.8126        | 14.78 | 11500 | 0.2290          | 0.2382 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0
