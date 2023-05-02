---
language:
- myv
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- myv
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-300m-myv-v1
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: myv
    metrics:
    - name: Test WER
      type: wer
      value: 0.599548532731377
    - name: Test CER
      type: cer
      value: 0.12953851902597
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: myv
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

# wav2vec2-large-xls-r-300m-myv-v1

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - MYV dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8537
- Wer: 0.6160

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-myv-v1 --dataset mozilla-foundation/common_voice_8_0 --config myv --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

Erzya language not found in speech-recognition-community-v2/dev_data!

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.000222
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 150
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 19.453        | 1.92   | 50   | 16.4001         | 1.0    |
| 9.6875        | 3.85   | 100  | 5.4468          | 1.0    |
| 4.9988        | 5.77   | 150  | 4.3507          | 1.0    |
| 4.1148        | 7.69   | 200  | 3.6753          | 1.0    |
| 3.4922        | 9.62   | 250  | 3.3103          | 1.0    |
| 3.2443        | 11.54  | 300  | 3.1741          | 1.0    |
| 3.164         | 13.46  | 350  | 3.1346          | 1.0    |
| 3.0954        | 15.38  | 400  | 3.0428          | 1.0    |
| 3.0076        | 17.31  | 450  | 2.9137          | 1.0    |
| 2.6883        | 19.23  | 500  | 2.1476          | 0.9978 |
| 1.5124        | 21.15  | 550  | 0.8955          | 0.8225 |
| 0.8711        | 23.08  | 600  | 0.6948          | 0.7591 |
| 0.6695        | 25.0   | 650  | 0.6683          | 0.7636 |
| 0.5606        | 26.92  | 700  | 0.6821          | 0.7435 |
| 0.503         | 28.85  | 750  | 0.7220          | 0.7516 |
| 0.4528        | 30.77  | 800  | 0.6638          | 0.7324 |
| 0.4219        | 32.69  | 850  | 0.7120          | 0.7435 |
| 0.4109        | 34.62  | 900  | 0.7122          | 0.7511 |
| 0.3887        | 36.54  | 950  | 0.7179          | 0.7199 |
| 0.3895        | 38.46  | 1000 | 0.7322          | 0.7525 |
| 0.391         | 40.38  | 1050 | 0.6850          | 0.7364 |
| 0.3537        | 42.31  | 1100 | 0.7571          | 0.7279 |
| 0.3267        | 44.23  | 1150 | 0.7575          | 0.7257 |
| 0.3195        | 46.15  | 1200 | 0.7580          | 0.6998 |
| 0.2891        | 48.08  | 1250 | 0.7452          | 0.7101 |
| 0.294         | 50.0   | 1300 | 0.7316          | 0.6945 |
| 0.2854        | 51.92  | 1350 | 0.7241          | 0.6757 |
| 0.2801        | 53.85  | 1400 | 0.7532          | 0.6887 |
| 0.2502        | 55.77  | 1450 | 0.7587          | 0.6811 |
| 0.2427        | 57.69  | 1500 | 0.7231          | 0.6851 |
| 0.2311        | 59.62  | 1550 | 0.7288          | 0.6632 |
| 0.2176        | 61.54  | 1600 | 0.7711          | 0.6664 |
| 0.2117        | 63.46  | 1650 | 0.7914          | 0.6940 |
| 0.2114        | 65.38  | 1700 | 0.8065          | 0.6918 |
| 0.1913        | 67.31  | 1750 | 0.8372          | 0.6945 |
| 0.1897        | 69.23  | 1800 | 0.8051          | 0.6869 |
| 0.1865        | 71.15  | 1850 | 0.8076          | 0.6740 |
| 0.1844        | 73.08  | 1900 | 0.7935          | 0.6708 |
| 0.1757        | 75.0   | 1950 | 0.8015          | 0.6610 |
| 0.1636        | 76.92  | 2000 | 0.7614          | 0.6414 |
| 0.1637        | 78.85  | 2050 | 0.8123          | 0.6592 |
| 0.1599        | 80.77  | 2100 | 0.7907          | 0.6566 |
| 0.1498        | 82.69  | 2150 | 0.8641          | 0.6757 |
| 0.1545        | 84.62  | 2200 | 0.7438          | 0.6682 |
| 0.1433        | 86.54  | 2250 | 0.8014          | 0.6624 |
| 0.1427        | 88.46  | 2300 | 0.7758          | 0.6646 |
| 0.1423        | 90.38  | 2350 | 0.7741          | 0.6423 |
| 0.1298        | 92.31  | 2400 | 0.7938          | 0.6414 |
| 0.1111        | 94.23  | 2450 | 0.7976          | 0.6467 |
| 0.1243        | 96.15  | 2500 | 0.7916          | 0.6481 |
| 0.1215        | 98.08  | 2550 | 0.7594          | 0.6392 |
| 0.113         | 100.0  | 2600 | 0.8236          | 0.6392 |
| 0.1077        | 101.92 | 2650 | 0.7959          | 0.6347 |
| 0.0988        | 103.85 | 2700 | 0.8189          | 0.6392 |
| 0.0953        | 105.77 | 2750 | 0.8157          | 0.6414 |
| 0.0889        | 107.69 | 2800 | 0.7946          | 0.6369 |
| 0.0929        | 109.62 | 2850 | 0.8255          | 0.6360 |
| 0.0822        | 111.54 | 2900 | 0.8320          | 0.6334 |
| 0.086         | 113.46 | 2950 | 0.8539          | 0.6490 |
| 0.0825        | 115.38 | 3000 | 0.8438          | 0.6418 |
| 0.0727        | 117.31 | 3050 | 0.8568          | 0.6481 |
| 0.0717        | 119.23 | 3100 | 0.8447          | 0.6512 |
| 0.0815        | 121.15 | 3150 | 0.8470          | 0.6445 |
| 0.0689        | 123.08 | 3200 | 0.8264          | 0.6249 |
| 0.0726        | 125.0  | 3250 | 0.7981          | 0.6169 |
| 0.0648        | 126.92 | 3300 | 0.8237          | 0.6200 |
| 0.0632        | 128.85 | 3350 | 0.8416          | 0.6249 |
| 0.06          | 130.77 | 3400 | 0.8276          | 0.6173 |
| 0.0616        | 132.69 | 3450 | 0.8429          | 0.6209 |
| 0.0614        | 134.62 | 3500 | 0.8485          | 0.6271 |
| 0.0539        | 136.54 | 3550 | 0.8598          | 0.6218 |
| 0.0555        | 138.46 | 3600 | 0.8557          | 0.6169 |
| 0.0604        | 140.38 | 3650 | 0.8436          | 0.6186 |
| 0.0556        | 142.31 | 3700 | 0.8428          | 0.6178 |
| 0.051         | 144.23 | 3750 | 0.8440          | 0.6142 |
| 0.0526        | 146.15 | 3800 | 0.8566          | 0.6142 |
| 0.052         | 148.08 | 3850 | 0.8544          | 0.6178 |
| 0.0519        | 150.0  | 3900 | 0.8537          | 0.6160 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.2
- Tokenizers 0.11.0
