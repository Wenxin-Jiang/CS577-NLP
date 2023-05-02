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
- name: wav2vec2-large-xls-r-300m-hsb-v2
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
      value: 0.4654228855721393
    - name: Test CER
      type: cer
      value: 0.11351049990708047
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

# wav2vec2-large-xls-r-300m-hsb-v2

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - HSB dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5328
- Wer: 0.4596

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-hsb-v2 --dataset mozilla-foundation/common_voice_8_0 --config hsb --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

Upper Sorbian (hsb) not found in speech-recognition-community-v2/dev_data


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
| 8.5979        | 3.23  | 100  | 3.5602          | 1.0    |
| 3.303         | 6.45  | 200  | 3.2238          | 1.0    |
| 3.2034        | 9.68  | 300  | 3.2002          | 0.9888 |
| 2.7986        | 12.9  | 400  | 1.2408          | 0.9210 |
| 1.3869        | 16.13 | 500  | 0.7973          | 0.7462 |
| 1.0228        | 19.35 | 600  | 0.6722          | 0.6788 |
| 0.8311        | 22.58 | 700  | 0.6100          | 0.6150 |
| 0.717         | 25.81 | 800  | 0.6236          | 0.6013 |
| 0.6264        | 29.03 | 900  | 0.6031          | 0.5575 |
| 0.5494        | 32.26 | 1000 | 0.5656          | 0.5309 |
| 0.4781        | 35.48 | 1100 | 0.5289          | 0.4996 |
| 0.4311        | 38.71 | 1200 | 0.5375          | 0.4768 |
| 0.3902        | 41.94 | 1300 | 0.5246          | 0.4703 |
| 0.3508        | 45.16 | 1400 | 0.5382          | 0.4696 |
| 0.3199        | 48.39 | 1500 | 0.5328          | 0.4596 |


### Framework versions

- Transformers 4.16.1
- Pytorch 1.10.0+cu111
- Datasets 1.18.2
- Tokenizers 0.11.0
 