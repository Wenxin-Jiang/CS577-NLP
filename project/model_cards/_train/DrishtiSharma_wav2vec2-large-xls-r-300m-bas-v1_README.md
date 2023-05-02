---
language:
- bas
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- bas
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-300m-bas-v1
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: bas
    metrics:
    - name: Test WER
      type: wer
      value: 0.3566497929130234
    - name: Test CER
      type: cer
      value: 0.1102657634184471
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: bas
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

# wav2vec2-large-xls-r-300m-bas-v1

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - BAS dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5997
- Wer: 0.3870

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-bas-v1 --dataset mozilla-foundation/common_voice_8_0 --config bas --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

Basaa (bas) language isn't available in speech-recognition-community-v2/dev_data

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.000111
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 100
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 12.7076       | 5.26  | 200  | 3.6361          | 1.0    |
| 3.1657        | 10.52 | 400  | 3.0101          | 1.0    |
| 2.3987        | 15.78 | 600  | 0.9125          | 0.6774 |
| 1.0079        | 21.05 | 800  | 0.6477          | 0.5352 |
| 0.7392        | 26.31 | 1000 | 0.5432          | 0.4929 |
| 0.6114        | 31.57 | 1200 | 0.5498          | 0.4639 |
| 0.5222        | 36.83 | 1400 | 0.5220          | 0.4561 |
| 0.4648        | 42.1  | 1600 | 0.5586          | 0.4289 |
| 0.4103        | 47.36 | 1800 | 0.5337          | 0.4082 |
| 0.3692        | 52.62 | 2000 | 0.5421          | 0.3861 |
| 0.3403        | 57.88 | 2200 | 0.5549          | 0.4096 |
| 0.3011        | 63.16 | 2400 | 0.5833          | 0.3925 |
| 0.2932        | 68.42 | 2600 | 0.5674          | 0.3815 |
| 0.2696        | 73.68 | 2800 | 0.5734          | 0.3889 |
| 0.2496        | 78.94 | 3000 | 0.5968          | 0.3985 |
| 0.2289        | 84.21 | 3200 | 0.5888          | 0.3893 |
| 0.2091        | 89.47 | 3400 | 0.5849          | 0.3852 |
| 0.2005        | 94.73 | 3600 | 0.5938          | 0.3875 |
| 0.1876        | 99.99 | 3800 | 0.5997          | 0.3870 |


### Framework versions

- Transformers 4.16.1
- Pytorch 1.10.0+cu111
- Datasets 1.18.2
- Tokenizers 0.11.0
