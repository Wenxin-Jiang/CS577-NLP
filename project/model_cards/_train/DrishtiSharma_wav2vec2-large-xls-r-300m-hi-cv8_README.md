---
language:
- hi
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- hi
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-300m-hi-cv8
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: hi
    metrics:
    - name: Test WER
      type: wer
      value: 0.3628727037755008
    - name: Test CER
      type: cer
      value: 0.11933724247521164
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

# wav2vec2-large-xls-r-300m-hi-cv8

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - HI  dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6510
- Wer: 0.3179

### Evaluation Commands
1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-hi-cv8 --dataset mozilla-foundation/common_voice_8_0 --config hi --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-hi-cv8 --dataset speech-recognition-community-v2/dev_data --config hi --split validation --chunk_length_s 10 --stride_length_s 1

Note: Hindi language not found in speech-recognition-community-v2/dev_data



### Training hyperparameters

The following hyperparameters were used during training:

- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 12.5576       | 1.04  | 200  | 6.6594          | 1.0    |
| 4.4069        | 2.07  | 400  | 3.6011          | 1.0    |
| 3.4273        | 3.11  | 600  | 3.3370          | 1.0    |
| 2.1108        | 4.15  | 800  | 1.0641          | 0.6562 |
| 0.8817        | 5.18  | 1000 | 0.7178          | 0.5172 |
| 0.6508        | 6.22  | 1200 | 0.6612          | 0.4839 |
| 0.5524        | 7.25  | 1400 | 0.6458          | 0.4889 |
| 0.4992        | 8.29  | 1600 | 0.5791          | 0.4382 |
| 0.4669        | 9.33  | 1800 | 0.6039          | 0.4352 |
| 0.4441        | 10.36 | 2000 | 0.6276          | 0.4297 |
| 0.4172        | 11.4  | 2200 | 0.6183          | 0.4474 |
| 0.3872        | 12.44 | 2400 | 0.5886          | 0.4231 |
| 0.3692        | 13.47 | 2600 | 0.6448          | 0.4399 |
| 0.3385        | 14.51 | 2800 | 0.6344          | 0.4075 |
| 0.3246        | 15.54 | 3000 | 0.5896          | 0.4087 |
| 0.3026        | 16.58 | 3200 | 0.6158          | 0.4016 |
| 0.284         | 17.62 | 3400 | 0.6038          | 0.3906 |
| 0.2682        | 18.65 | 3600 | 0.6165          | 0.3900 |
| 0.2577        | 19.69 | 3800 | 0.5754          | 0.3805 |
| 0.2509        | 20.73 | 4000 | 0.6028          | 0.3925 |
| 0.2426        | 21.76 | 4200 | 0.6335          | 0.4138 |
| 0.2346        | 22.8  | 4400 | 0.6128          | 0.3870 |
| 0.2205        | 23.83 | 4600 | 0.6223          | 0.3831 |
| 0.2104        | 24.87 | 4800 | 0.6122          | 0.3781 |
| 0.1992        | 25.91 | 5000 | 0.6467          | 0.3792 |
| 0.1916        | 26.94 | 5200 | 0.6277          | 0.3636 |
| 0.1835        | 27.98 | 5400 | 0.6317          | 0.3773 |
| 0.1776        | 29.02 | 5600 | 0.6124          | 0.3614 |
| 0.1751        | 30.05 | 5800 | 0.6475          | 0.3628 |
| 0.1662        | 31.09 | 6000 | 0.6266          | 0.3504 |
| 0.1584        | 32.12 | 6200 | 0.6347          | 0.3532 |
| 0.1494        | 33.16 | 6400 | 0.6636          | 0.3491 |
| 0.1457        | 34.2  | 6600 | 0.6334          | 0.3507 |
| 0.1427        | 35.23 | 6800 | 0.6397          | 0.3442 |
| 0.1397        | 36.27 | 7000 | 0.6468          | 0.3496 |
| 0.1283        | 37.31 | 7200 | 0.6291          | 0.3416 |
| 0.1255        | 38.34 | 7400 | 0.6652          | 0.3461 |
| 0.1195        | 39.38 | 7600 | 0.6587          | 0.3342 |
| 0.1169        | 40.41 | 7800 | 0.6478          | 0.3319 |
| 0.1126        | 41.45 | 8000 | 0.6280          | 0.3291 |
| 0.1112        | 42.49 | 8200 | 0.6434          | 0.3290 |
| 0.1069        | 43.52 | 8400 | 0.6542          | 0.3268 |
| 0.1027        | 44.56 | 8600 | 0.6536          | 0.3239 |
| 0.0993        | 45.6  | 8800 | 0.6622          | 0.3257 |
| 0.0973        | 46.63 | 9000 | 0.6572          | 0.3192 |
| 0.0911        | 47.67 | 9200 | 0.6522          | 0.3175 |
| 0.0897        | 48.7  | 9400 | 0.6521          | 0.3200 |
| 0.0905        | 49.74 | 9600 | 0.6510          | 0.3179 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
