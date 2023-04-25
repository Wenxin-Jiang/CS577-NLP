---
language:
- ar
license: apache-2.0
tags:
- ar
- automatic-speech-recognition
- generated_from_trainer
- hf-asr-leaderboard
- mozilla-foundation/common_voice_7_0
- robust-speech-event
datasets:
- mozilla-foundation/common_voice_7_0
model-index:
- name: XLS-R-300M - Arabic
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 7
      type: mozilla-foundation/common_voice_7_0
      args: ar
    metrics:
    - name: Test WER
      type: wer
      value: 47.54
    - name: Test CER
      type: cer
      value: 17.64
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: ar
    metrics:
    - name: Test WER
      type: wer
      value: 93.72
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: ar
    metrics:
    - name: Test WER
      type: wer
      value: 92.49
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_7_0 - AR dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4502
- Wer: 0.4783

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 5.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 4.7972        | 0.43  | 500   | 5.1401          | 1.0    |
| 3.3241        | 0.86  | 1000  | 3.3220          | 1.0    |
| 3.1432        | 1.29  | 1500  | 3.0806          | 0.9999 |
| 2.9297        | 1.72  | 2000  | 2.5678          | 1.0057 |
| 2.2593        | 2.14  | 2500  | 1.1068          | 0.8218 |
| 2.0504        | 2.57  | 3000  | 0.7878          | 0.7114 |
| 1.937         | 3.0   | 3500  | 0.6955          | 0.6450 |
| 1.8491        | 3.43  | 4000  | 0.6452          | 0.6304 |
| 1.803         | 3.86  | 4500  | 0.5961          | 0.6042 |
| 1.7545        | 4.29  | 5000  | 0.5550          | 0.5748 |
| 1.7045        | 4.72  | 5500  | 0.5374          | 0.5743 |
| 1.6733        | 5.15  | 6000  | 0.5337          | 0.5404 |
| 1.6761        | 5.57  | 6500  | 0.5054          | 0.5266 |
| 1.655         | 6.0   | 7000  | 0.4926          | 0.5243 |
| 1.6252        | 6.43  | 7500  | 0.4946          | 0.5183 |
| 1.6209        | 6.86  | 8000  | 0.4915          | 0.5194 |
| 1.5772        | 7.29  | 8500  | 0.4725          | 0.5104 |
| 1.5602        | 7.72  | 9000  | 0.4726          | 0.5097 |
| 1.5783        | 8.15  | 9500  | 0.4667          | 0.4956 |
| 1.5442        | 8.58  | 10000 | 0.4685          | 0.4937 |
| 1.5597        | 9.01  | 10500 | 0.4708          | 0.4957 |
| 1.5406        | 9.43  | 11000 | 0.4539          | 0.4810 |
| 1.5274        | 9.86  | 11500 | 0.4502          | 0.4783 |


### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.17.1.dev0
- Tokenizers 0.11.0
