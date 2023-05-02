---
language:
- rm-sursilv
license: apache-2.0
tags:
- automatic-speech-recognition
- hf-asr-leaderboard
- robust-speech-event
datasets:
- mozilla-foundation/common_voice_8_0
metrics:
- wer
model-index:
- name: wav2vec2-xls-r-300m-rm-sursilv-d11
  results:
  - task:
      type: automatic-speech-recognition
      name: Speech Recognition
    dataset:
      type: mozilla-foundation/common_voice_8_0
      name: Common Voice 8
      args: rm-sursilv
    metrics:
    - type: wer
      value: 0.24094169578811844
      name: Test WER
    - name: Test CER
      type: cer
      value: 0.049832791672554284
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: rm-sursilv
    metrics:
    - name: Test WER
      type: wer
      value: NA
    - name: Test CER
      type: cer
      value: NA
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - RM-SURSILV dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2511
- Wer: 0.2415 

#### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-xls-r-300m-rm-sursilv-d11 --dataset mozilla-foundation/common_voice_8_0 --config rm-sursilv --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

Romansh-Sursilv language isn't available in speech-recognition-community-v2/dev_data



### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7e-05
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 125.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Wer    |
|:-------------:|:------:|:-----:|:---------------:|:------:|
| 2.3958        | 17.44  | 1500  | 0.6808          | 0.6521 |
| 0.9663        | 34.88  | 3000  | 0.3023          | 0.3718 |
| 0.7963        | 52.33  | 4500  | 0.2588          | 0.3046 |
| 0.6893        | 69.77  | 6000  | 0.2436          | 0.2718 |
| 0.6148        | 87.21  | 7500  | 0.2521          | 0.2572 |
| 0.5556        | 104.65 | 9000  | 0.2490          | 0.2442 |
| 0.5258        | 122.09 | 10500 | 0.2515          | 0.2442 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0
