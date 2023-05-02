---
language:
- hi
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_7_0
- generated_from_trainer
- hi
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_7_0
model-index:
- name: wav2vec2-large-xls-r-300m-hi-d3
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 7
      type: mozilla-foundation/common_voice_7_0
      args: vot
    metrics:
    - name: Test WER
      type: wer
      value: 0.4204111781361566
    - name: Test CER
      type: cer
      value: 0.13869169624556316
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: hi
    metrics:
    - name: Test WER
      type: wer
      value: NA
    - name: Test CER
      type: cer
      value: NA
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 7.0
      type: mozilla-foundation/common_voice_7_0
      args: hi
    metrics:
    - name: Test WER
      type: wer
      value: 42.04
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-hi-d3

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_7_0 - HI dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7988
- Wer: 0.3713

###Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-hi-d3 --dataset mozilla-foundation/common_voice_7_0 --config hi --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

Hindi language isn't available in speech-recognition-community-v2/dev_data

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.000388
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 750
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 8.2826        | 1.36  | 200  | 3.5253          | 1.0    |
| 2.7019        | 2.72  | 400  | 1.1744          | 0.7360 |
| 0.7358        | 4.08  | 600  | 0.7781          | 0.5501 |
| 0.4942        | 5.44  | 800  | 0.7590          | 0.5345 |
| 0.4056        | 6.8   | 1000 | 0.6885          | 0.4776 |
| 0.3243        | 8.16  | 1200 | 0.7195          | 0.4861 |
| 0.2785        | 9.52  | 1400 | 0.7473          | 0.4930 |
| 0.2448        | 10.88 | 1600 | 0.7201          | 0.4574 |
| 0.2155        | 12.24 | 1800 | 0.7686          | 0.4648 |
| 0.2039        | 13.6  | 2000 | 0.7440          | 0.4624 |
| 0.1792        | 14.96 | 2200 | 0.7815          | 0.4658 |
| 0.1695        | 16.33 | 2400 | 0.7678          | 0.4557 |
| 0.1598        | 17.68 | 2600 | 0.7468          | 0.4393 |
| 0.1568        | 19.05 | 2800 | 0.7440          | 0.4422 |
| 0.1391        | 20.41 | 3000 | 0.7656          | 0.4317 |
| 0.1283        | 21.77 | 3200 | 0.7892          | 0.4299 |
| 0.1194        | 23.13 | 3400 | 0.7646          | 0.4192 |
| 0.1116        | 24.49 | 3600 | 0.8156          | 0.4330 |
| 0.1111        | 25.85 | 3800 | 0.7661          | 0.4322 |
| 0.1023        | 27.21 | 4000 | 0.7419          | 0.4276 |
| 0.1007        | 28.57 | 4200 | 0.8488          | 0.4245 |
| 0.0925        | 29.93 | 4400 | 0.8062          | 0.4070 |
| 0.0918        | 31.29 | 4600 | 0.8412          | 0.4218 |
| 0.0813        | 32.65 | 4800 | 0.8045          | 0.4087 |
| 0.0805        | 34.01 | 5000 | 0.8411          | 0.4113 |
| 0.0774        | 35.37 | 5200 | 0.7664          | 0.3943 |
| 0.0666        | 36.73 | 5400 | 0.8082          | 0.3939 |
| 0.0655        | 38.09 | 5600 | 0.7948          | 0.4000 |
| 0.0617        | 39.45 | 5800 | 0.8084          | 0.3932 |
| 0.0606        | 40.81 | 6000 | 0.8223          | 0.3841 |
| 0.0569        | 42.18 | 6200 | 0.7892          | 0.3832 |
| 0.0544        | 43.54 | 6400 | 0.8326          | 0.3834 |
| 0.0508        | 44.89 | 6600 | 0.7952          | 0.3774 |
| 0.0492        | 46.26 | 6800 | 0.7923          | 0.3756 |
| 0.0459        | 47.62 | 7000 | 0.7925          | 0.3701 |
| 0.0423        | 48.98 | 7200 | 0.7988          | 0.3713 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
