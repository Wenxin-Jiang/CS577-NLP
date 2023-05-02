---
language:
- br
license: apache-2.0
tags:
- generated_from_trainer
- robust-speech-event
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
metrics:
- wer
model-index:
- name: wav2vec2-large-xls-r-300m-br-d10
  results:
  - task:
      type: automatic-speech-recognition
      name: Speech Recognition
    dataset:
      type: mozilla-foundation/common_voice_8_0
      name: Common Voice 8
      args: br
    metrics:
    - type: wer
      value: 0.5230357484228637
      name: Test WER
    - name: Test CER
      type: cer
      value: 0.1880661144228536
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: br
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

# wav2vec2-large-xls-r-300m-br-d10

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - BR dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1382
- Wer: 0.4895


### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-br-d10 --dataset mozilla-foundation/common_voice_8_0 --config br --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

Breton language isn't available in speech-recognition-community-v2/dev_data


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0004
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 800
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 13.611        | 0.68  | 100  | 5.8492          | 1.0    |
| 3.8176        | 1.35  | 200  | 3.2181          | 1.0    |
| 3.0457        | 2.03  | 300  | 3.0902          | 1.0    |
| 2.2632        | 2.7   | 400  | 1.4882          | 0.9426 |
| 1.1965        | 3.38  | 500  | 1.1396          | 0.7950 |
| 0.984         | 4.05  | 600  | 1.0216          | 0.7583 |
| 0.8036        | 4.73  | 700  | 1.0258          | 0.7202 |
| 0.7061        | 5.41  | 800  | 0.9710          | 0.6820 |
| 0.689         | 6.08  | 900  | 0.9731          | 0.6488 |
| 0.6063        | 6.76  | 1000 | 0.9442          | 0.6569 |
| 0.5215        | 7.43  | 1100 | 1.0221          | 0.6671 |
| 0.4965        | 8.11  | 1200 | 0.9266          | 0.6181 |
| 0.4321        | 8.78  | 1300 | 0.9050          | 0.5991 |
| 0.3762        | 9.46  | 1400 | 0.9801          | 0.6134 |
| 0.3747        | 10.14 | 1500 | 0.9210          | 0.5747 |
| 0.3554        | 10.81 | 1600 | 0.9720          | 0.6051 |
| 0.3148        | 11.49 | 1700 | 0.9672          | 0.6099 |
| 0.3176        | 12.16 | 1800 | 1.0120          | 0.5966 |
| 0.2915        | 12.84 | 1900 | 0.9490          | 0.5653 |
| 0.2696        | 13.51 | 2000 | 0.9394          | 0.5819 |
| 0.2569        | 14.19 | 2100 | 1.0197          | 0.5667 |
| 0.2395        | 14.86 | 2200 | 0.9771          | 0.5608 |
| 0.2367        | 15.54 | 2300 | 1.0516          | 0.5678 |
| 0.2153        | 16.22 | 2400 | 1.0097          | 0.5679 |
| 0.2092        | 16.89 | 2500 | 1.0143          | 0.5430 |
| 0.2046        | 17.57 | 2600 | 1.0884          | 0.5631 |
| 0.1937        | 18.24 | 2700 | 1.0113          | 0.5648 |
| 0.1752        | 18.92 | 2800 | 1.0056          | 0.5470 |
| 0.164         | 19.59 | 2900 | 1.0340          | 0.5508 |
| 0.1723        | 20.27 | 3000 | 1.0743          | 0.5615 |
| 0.1535        | 20.95 | 3100 | 1.0495          | 0.5465 |
| 0.1432        | 21.62 | 3200 | 1.0390          | 0.5333 |
| 0.1561        | 22.3  | 3300 | 1.0798          | 0.5590 |
| 0.1384        | 22.97 | 3400 | 1.1716          | 0.5449 |
| 0.1359        | 23.65 | 3500 | 1.1154          | 0.5420 |
| 0.1356        | 24.32 | 3600 | 1.0883          | 0.5387 |
| 0.1355        | 25.0  | 3700 | 1.1114          | 0.5504 |
| 0.1158        | 25.68 | 3800 | 1.1171          | 0.5388 |
| 0.1166        | 26.35 | 3900 | 1.1335          | 0.5403 |
| 0.1165        | 27.03 | 4000 | 1.1374          | 0.5248 |
| 0.1064        | 27.7  | 4100 | 1.0336          | 0.5298 |
| 0.0987        | 28.38 | 4200 | 1.0407          | 0.5216 |
| 0.104         | 29.05 | 4300 | 1.1012          | 0.5350 |
| 0.0894        | 29.73 | 4400 | 1.1016          | 0.5310 |
| 0.0912        | 30.41 | 4500 | 1.1383          | 0.5302 |
| 0.0972        | 31.08 | 4600 | 1.0851          | 0.5214 |
| 0.0832        | 31.76 | 4700 | 1.1705          | 0.5311 |
| 0.0859        | 32.43 | 4800 | 1.0750          | 0.5192 |
| 0.0811        | 33.11 | 4900 | 1.0900          | 0.5180 |
| 0.0825        | 33.78 | 5000 | 1.1271          | 0.5196 |
| 0.07          | 34.46 | 5100 | 1.1289          | 0.5141 |
| 0.0689        | 35.14 | 5200 | 1.0960          | 0.5101 |
| 0.068         | 35.81 | 5300 | 1.1377          | 0.5050 |
| 0.0776        | 36.49 | 5400 | 1.0880          | 0.5194 |
| 0.0642        | 37.16 | 5500 | 1.1027          | 0.5076 |
| 0.0607        | 37.84 | 5600 | 1.1293          | 0.5119 |
| 0.0607        | 38.51 | 5700 | 1.1229          | 0.5103 |
| 0.0545        | 39.19 | 5800 | 1.1168          | 0.5103 |
| 0.0562        | 39.86 | 5900 | 1.1206          | 0.5073 |
| 0.0484        | 40.54 | 6000 | 1.1710          | 0.5019 |
| 0.0499        | 41.22 | 6100 | 1.1511          | 0.5100 |
| 0.0455        | 41.89 | 6200 | 1.1488          | 0.5009 |
| 0.0475        | 42.57 | 6300 | 1.1196          | 0.4944 |
| 0.0413        | 43.24 | 6400 | 1.1654          | 0.4996 |
| 0.0389        | 43.92 | 6500 | 1.0961          | 0.4930 |
| 0.0428        | 44.59 | 6600 | 1.0955          | 0.4938 |
| 0.039         | 45.27 | 6700 | 1.1323          | 0.4955 |
| 0.0352        | 45.95 | 6800 | 1.1040          | 0.4930 |
| 0.0334        | 46.62 | 6900 | 1.1382          | 0.4942 |
| 0.0338        | 47.3  | 7000 | 1.1264          | 0.4911 |
| 0.0307        | 47.97 | 7100 | 1.1216          | 0.4881 |
| 0.0286        | 48.65 | 7200 | 1.1459          | 0.4894 |
| 0.0348        | 49.32 | 7300 | 1.1419          | 0.4906 |
| 0.0329        | 50.0  | 7400 | 1.1382          | 0.4895 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
