
---
license: apache-2.0
tags:
- generated_from_trainer
- automatic-speech-recognition
- NbAiLab/NPSC
- robust-speech-event
- false
- nb-NO
- hf-asr-leaderboard
datasets:
- NbAiLab/NPSC
language:
- nb-NO
model-index:
- name: wav2vec2-xls-r-1b-npsc-bokmaal
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: NPSC
      type: NbAiLab/NPSC
      args: 16K_mp3_bokmaal
    metrics:
    - name: "Test (Bokm\xE5l) WER"
      type: wer
      value: 0.07901700231893541
    - name: "Test (Bokm\xE5l) CER"
      type: cer
      value: 0.029734583252347752
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-1b-npsc

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-1b](https://huggingface.co/facebook/wav2vec2-xls-r-1b) on the [NbAiLab/NPSC (16K_mp3_bokmaal)](https://huggingface.co/datasets/NbAiLab/NPSC/viewer/16K_mp3_bokmaal/train) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1598
- WER: 0.0966

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 15.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 0.8361        | 0.32  | 500   | 0.6304          | 0.4970 |
| 0.5703        | 0.64  | 1000  | 0.3195          | 0.2775 |
| 0.5451        | 0.97  | 1500  | 0.2700          | 0.2246 |
| 0.47          | 1.29  | 2000  | 0.2564          | 0.2329 |
| 0.4063        | 1.61  | 2500  | 0.2459          | 0.2099 |
| 0.374         | 1.93  | 3000  | 0.2175          | 0.1894 |
| 0.3297        | 2.26  | 3500  | 0.2036          | 0.1755 |
| 0.3145        | 2.58  | 4000  | 0.1957          | 0.1757 |
| 0.3989        | 2.9   | 4500  | 0.1923          | 0.1723 |
| 0.271         | 3.22  | 5000  | 0.1889          | 0.1649 |
| 0.2758        | 3.55  | 5500  | 0.1768          | 0.1588 |
| 0.2683        | 3.87  | 6000  | 0.1720          | 0.1534 |
| 0.2341        | 4.19  | 6500  | 0.1689          | 0.1471 |
| 0.2316        | 4.51  | 7000  | 0.1706          | 0.1405 |
| 0.2383        | 4.84  | 7500  | 0.1637          | 0.1426 |
| 0.2148        | 5.16  | 8000  | 0.1584          | 0.1347 |
| 0.2085        | 5.48  | 8500  | 0.1601          | 0.1387 |
| 0.2944        | 5.8   | 9000  | 0.1566          | 0.1294 |
| 0.1944        | 6.13  | 9500  | 0.1494          | 0.1271 |
| 0.1853        | 6.45  | 10000 | 0.1561          | 0.1247 |
| 0.235         | 6.77  | 10500 | 0.1461          | 0.1215 |
| 0.2286        | 7.09  | 11000 | 0.1447          | 0.1167 |
| 0.1781        | 7.41  | 11500 | 0.1502          | 0.1199 |
| 0.1714        | 7.74  | 12000 | 0.1425          | 0.1179 |
| 0.1725        | 8.06  | 12500 | 0.1427          | 0.1173 |
| 0.143         | 8.38  | 13000 | 0.1448          | 0.1142 |
| 0.154         | 8.7   | 13500 | 0.1392          | 0.1104 |
| 0.1447        | 9.03  | 14000 | 0.1404          | 0.1094 |
| 0.1471        | 9.35  | 14500 | 0.1404          | 0.1088 |
| 0.1479        | 9.67  | 15000 | 0.1414          | 0.1133 |
| 0.1607        | 9.99  | 15500 | 0.1458          | 0.1171 |
| 0.166         | 10.32 | 16000 | 0.1652          | 0.1264 |
| 0.188         | 10.64 | 16500 | 0.1713          | 0.1322 |
| 0.1461        | 10.96 | 17000 | 0.1423          | 0.1111 |
| 0.1289        | 11.28 | 17500 | 0.1388          | 0.1097 |
| 0.1273        | 11.61 | 18000 | 0.1438          | 0.1074 |
| 0.1317        | 11.93 | 18500 | 0.1312          | 0.1066 |
| 0.1448        | 12.25 | 19000 | 0.1446          | 0.1042 |
| 0.1424        | 12.57 | 19500 | 0.1386          | 0.1015 |
| 0.1392        | 12.89 | 20000 | 0.1379          | 0.1005 |
| 0.1408        | 13.22 | 20500 | 0.1408          | 0.0992 |
| 0.1239        | 13.54 | 21000 | 0.1338          | 0.0968 |
| 0.1244        | 13.86 | 21500 | 0.1335          | 0.0957 |
| 0.1254        | 14.18 | 22000 | 0.1382          | 0.0950 |
| 0.1597        | 14.51 | 22500 | 0.1544          | 0.0970 |
| 0.1566        | 14.83 | 23000 | 0.1589          | 0.0963 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu113
- Datasets 1.18.3.dev0
- Tokenizers 0.11.0
