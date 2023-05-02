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
      value: 62.47
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - UR dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8888
- Wer: 0.6642

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
| 10.1224       | 1.96  | 100  | 3.5429          | 1.0    |
| 3.2411        | 3.92  | 200  | 3.1786          | 1.0    |
| 3.1283        | 5.88  | 300  | 3.0571          | 1.0    |
| 3.0044        | 7.84  | 400  | 2.9560          | 0.9996 |
| 2.9388        | 9.8   | 500  | 2.8977          | 1.0011 |
| 2.86          | 11.76 | 600  | 2.6944          | 0.9952 |
| 2.5538        | 13.73 | 700  | 2.0967          | 0.9435 |
| 2.1214        | 15.69 | 800  | 1.4816          | 0.8428 |
| 1.8136        | 17.65 | 900  | 1.2459          | 0.8048 |
| 1.6795        | 19.61 | 1000 | 1.1232          | 0.7649 |
| 1.5571        | 21.57 | 1100 | 1.0510          | 0.7432 |
| 1.4975        | 23.53 | 1200 | 1.0298          | 0.6963 |
| 1.4485        | 25.49 | 1300 | 0.9775          | 0.7074 |
| 1.3924        | 27.45 | 1400 | 0.9798          | 0.6956 |
| 1.3604        | 29.41 | 1500 | 0.9345          | 0.7092 |
| 1.3224        | 31.37 | 1600 | 0.9535          | 0.6830 |
| 1.2816        | 33.33 | 1700 | 0.9178          | 0.6679 |
| 1.2623        | 35.29 | 1800 | 0.9249          | 0.6679 |
| 1.2421        | 37.25 | 1900 | 0.9124          | 0.6734 |
| 1.2208        | 39.22 | 2000 | 0.8962          | 0.6664 |
| 1.2145        | 41.18 | 2100 | 0.8903          | 0.6734 |
| 1.1888        | 43.14 | 2200 | 0.8883          | 0.6708 |
| 1.1933        | 45.1  | 2300 | 0.8928          | 0.6723 |
| 1.1838        | 47.06 | 2400 | 0.8868          | 0.6679 |
| 1.1634        | 49.02 | 2500 | 0.8886          | 0.6657 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0
