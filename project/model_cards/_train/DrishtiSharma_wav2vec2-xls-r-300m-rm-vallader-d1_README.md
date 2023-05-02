---
language:
- rm-vallader
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- rm-vallader
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-xls-r-300m-rm-vallader-d1
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: rm-vallader
    metrics:
    - name: Test WER
      type: wer
      value: 0.26472007722007723
    - name: Test CER
      type: cer
      value: 0.05860608074430969
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: vot
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

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - RM-VALLADER dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2754
- Wer: 0.2831


### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-xls-r-300m-rm-vallader-d1 --dataset mozilla-foundation/common_voice_8_0 --config rm-vallader --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

Romansh-Vallader language not found in speech-recognition-community-v2/dev_data


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 100.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 2.927         | 15.15 | 500  | 2.9196          | 1.0    |
| 1.3835        | 30.3  | 1000 | 0.5879          | 0.5866 |
| 0.7415        | 45.45 | 1500 | 0.3077          | 0.3316 |
| 0.5575        | 60.61 | 2000 | 0.2735          | 0.2954 |
| 0.4581        | 75.76 | 2500 | 0.2707          | 0.2802 |
| 0.3977        | 90.91 | 3000 | 0.2785          | 0.2809 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0
