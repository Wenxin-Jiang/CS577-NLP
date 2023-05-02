---
language:
- mt
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- mt
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-xls-r-300m-mt-o1
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: mt
    metrics:
    - name: Test WER
      type: wer
      value: 0.2378369069146646
    - name: Test CER
      type: cer
      value: 0.050364163712536256
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: mt
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

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - MT dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1987
- Wer: 0.1920

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-xls-r-300m-mt-o1 --dataset mozilla-foundation/common_voice_8_0 --config mt --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

Maltese language not found in speech-recognition-community-v2/dev_data!


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7e-05
- train_batch_size: 32
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 100.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 1.1721        | 18.02 | 2000  | 0.3831          | 0.4066 |
| 0.7849        | 36.04 | 4000  | 0.2191          | 0.2417 |
| 0.6723        | 54.05 | 6000  | 0.2056          | 0.2134 |
| 0.6015        | 72.07 | 8000  | 0.2008          | 0.2031 |
| 0.5386        | 90.09 | 10000 | 0.1967          | 0.1953 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0
