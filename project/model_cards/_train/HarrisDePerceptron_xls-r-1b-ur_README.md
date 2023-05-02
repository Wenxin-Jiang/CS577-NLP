---
language:
- ur
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- ur
- robust-speech-event
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: ''
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8.0
      type: mozilla-foundation/common_voice_8_0
      args: ur
    metrics:
    - name: Test WER
      type: wer
      value: 44.13
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-1b](https://huggingface.co/facebook/wav2vec2-xls-r-1b) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - UR dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9613
- Wer: 0.5376

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
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 50
- num_epochs: 50.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 5.3118        | 1.96  | 100  | 2.9093          | 0.9982 |
| 2.2071        | 3.92  | 200  | 1.1737          | 0.7779 |
| 1.6098        | 5.88  | 300  | 0.9984          | 0.7015 |
| 1.4333        | 7.84  | 400  | 0.9800          | 0.6705 |
| 1.2859        | 9.8   | 500  | 0.9582          | 0.6487 |
| 1.2073        | 11.76 | 600  | 0.8841          | 0.6077 |
| 1.1417        | 13.73 | 700  | 0.9118          | 0.6343 |
| 1.0988        | 15.69 | 800  | 0.9217          | 0.6196 |
| 1.0279        | 17.65 | 900  | 0.9165          | 0.5867 |
| 0.9765        | 19.61 | 1000 | 0.9306          | 0.5978 |
| 0.9161        | 21.57 | 1100 | 0.9305          | 0.5768 |
| 0.8395        | 23.53 | 1200 | 0.9828          | 0.5819 |
| 0.8306        | 25.49 | 1300 | 0.9397          | 0.5760 |
| 0.7819        | 27.45 | 1400 | 0.9544          | 0.5742 |
| 0.7509        | 29.41 | 1500 | 0.9278          | 0.5690 |
| 0.7218        | 31.37 | 1600 | 0.9003          | 0.5587 |
| 0.6725        | 33.33 | 1700 | 0.9659          | 0.5554 |
| 0.6287        | 35.29 | 1800 | 0.9522          | 0.5561 |
| 0.6077        | 37.25 | 1900 | 0.9154          | 0.5465 |
| 0.5873        | 39.22 | 2000 | 0.9331          | 0.5469 |
| 0.5621        | 41.18 | 2100 | 0.9335          | 0.5491 |
| 0.5168        | 43.14 | 2200 | 0.9632          | 0.5458 |
| 0.5114        | 45.1  | 2300 | 0.9349          | 0.5387 |
| 0.4986        | 47.06 | 2400 | 0.9364          | 0.5380 |
| 0.4761        | 49.02 | 2500 | 0.9584          | 0.5391 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0
