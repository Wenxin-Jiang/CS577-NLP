---
language:
- hsb
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- hsb
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-300m-hsb-v3
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: hsb
    metrics:
    - name: Test WER
      type: wer
      value: 0.4763681592039801
    - name: Test CER
      type: cer
      value: 0.11194945177476305
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: hsb
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

# wav2vec2-large-xls-r-300m-hsb-v3

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - HSB dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6549
- Wer: 0.4827

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-hsb-v3 --dataset mozilla-foundation/common_voice_8_0 --config hsb --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

Upper Sorbian (hsb) language not found in speech-recognition-community-v2/dev_data!

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.00045
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 8.8951        | 3.23  | 100  | 3.6396          | 1.0    |
| 3.314         | 6.45  | 200  | 3.2331          | 1.0    |
| 3.1931        | 9.68  | 300  | 3.0947          | 0.9906 |
| 1.7079        | 12.9  | 400  | 0.8865          | 0.8499 |
| 0.6859        | 16.13 | 500  | 0.7994          | 0.7529 |
| 0.4804        | 19.35 | 600  | 0.7783          | 0.7069 |
| 0.3506        | 22.58 | 700  | 0.6904          | 0.6321 |
| 0.2695        | 25.81 | 800  | 0.6519          | 0.5926 |
| 0.222         | 29.03 | 900  | 0.7041          | 0.5720 |
| 0.1828        | 32.26 | 1000 | 0.6608          | 0.5513 |
| 0.1474        | 35.48 | 1100 | 0.7129          | 0.5319 |
| 0.1269        | 38.71 | 1200 | 0.6664          | 0.5056 |
| 0.1077        | 41.94 | 1300 | 0.6712          | 0.4942 |
| 0.0934        | 45.16 | 1400 | 0.6467          | 0.4879 |
| 0.0819        | 48.39 | 1500 | 0.6549          | 0.4827 |


### Framework versions

- Transformers 4.16.1
- Pytorch 1.10.0+cu111
- Datasets 1.18.2
- Tokenizers 0.11.0
