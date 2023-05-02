---
language:
- hi
license: apache-2.0
tags:
- automatic-speech-recognition
- robust-speech-event
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
metrics:
- wer
model-index:
- name: wav2vec2-large-xls-r-300m-hi-cv8-b2
  results:
  - task:
      type: automatic-speech-recognition
      name: Speech Recognition
    dataset:
      type: mozilla-foundation/common_voice_8_0
      name: Common Voice 7
      args: hi
    metrics:
    - type: wer
      value: 0.3891350503092403
      name: Test WER
    - name: Test CER
      type: cer
      value: 0.13016327327131985
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
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-hi-cv8-b2

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - HI dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7322
- Wer: 0.3469

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-hi-cv8-b2 --dataset mozilla-foundation/common_voice_8_0 --config hi --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

Hindi language isn't available in speech-recognition-community-v2/dev_data


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.00025
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 700
- num_epochs: 35
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 9.6226        | 1.04  | 200  | 3.8855          | 1.0    |
| 3.4678        | 2.07  | 400  | 3.4283          | 1.0    |
| 2.3668        | 3.11  | 600  | 1.0743          | 0.7175 |
| 0.7308        | 4.15  | 800  | 0.7663          | 0.5498 |
| 0.4985        | 5.18  | 1000 | 0.6957          | 0.5001 |
| 0.3817        | 6.22  | 1200 | 0.6932          | 0.4866 |
| 0.3281        | 7.25  | 1400 | 0.7034          | 0.4983 |
| 0.2752        | 8.29  | 1600 | 0.6588          | 0.4606 |
| 0.2475        | 9.33  | 1800 | 0.6514          | 0.4328 |
| 0.219         | 10.36 | 2000 | 0.6396          | 0.4176 |
| 0.2036        | 11.4  | 2200 | 0.6867          | 0.4162 |
| 0.1793        | 12.44 | 2400 | 0.6943          | 0.4196 |
| 0.1724        | 13.47 | 2600 | 0.6862          | 0.4260 |
| 0.1554        | 14.51 | 2800 | 0.7615          | 0.4222 |
| 0.151         | 15.54 | 3000 | 0.7058          | 0.4110 |
| 0.1335        | 16.58 | 3200 | 0.7172          | 0.3986 |
| 0.1326        | 17.62 | 3400 | 0.7182          | 0.3923 |
| 0.1225        | 18.65 | 3600 | 0.6995          | 0.3910 |
| 0.1146        | 19.69 | 3800 | 0.7075          | 0.3875 |
| 0.108         | 20.73 | 4000 | 0.7297          | 0.3858 |
| 0.1048        | 21.76 | 4200 | 0.7413          | 0.3850 |
| 0.0979        | 22.8  | 4400 | 0.7452          | 0.3793 |
| 0.0946        | 23.83 | 4600 | 0.7436          | 0.3759 |
| 0.0897        | 24.87 | 4800 | 0.7289          | 0.3754 |
| 0.0854        | 25.91 | 5000 | 0.7271          | 0.3667 |
| 0.0803        | 26.94 | 5200 | 0.7378          | 0.3656 |
| 0.0752        | 27.98 | 5400 | 0.7488          | 0.3680 |
| 0.0718        | 29.02 | 5600 | 0.7185          | 0.3619 |
| 0.0702        | 30.05 | 5800 | 0.7428          | 0.3554 |
| 0.0653        | 31.09 | 6000 | 0.7447          | 0.3559 |
| 0.0638        | 32.12 | 6200 | 0.7327          | 0.3523 |
| 0.058         | 33.16 | 6400 | 0.7339          | 0.3488 |
| 0.0594        | 34.2  | 6600 | 0.7322          | 0.3469 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
