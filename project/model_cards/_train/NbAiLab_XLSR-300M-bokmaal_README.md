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
- name: XLSR-300M-bokmaal
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
      value: 0.07699635320946434
    - name: "Test (Bokm\xE5l) CER"
      type: cer
      value: 0.0284288464829
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# XLSR-300M-bokmaal

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the NBAILAB/NPSC - 16K_MP3_BOKMAAL dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1635
- Wer: 0.1005

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
| 3.0307        | 0.32  | 500   | 3.0026          | 1.0    |
| 2.7865        | 0.64  | 1000  | 2.4849          | 0.9926 |
| 0.7522        | 0.95  | 1500  | 0.4567          | 0.3594 |
| 0.5703        | 1.27  | 2000  | 0.3440          | 0.2586 |
| 0.4762        | 1.59  | 2500  | 0.2925          | 0.2178 |
| 0.4585        | 1.91  | 3000  | 0.2442          | 0.1981 |
| 0.4013        | 2.23  | 3500  | 0.2495          | 0.1818 |
| 0.449         | 2.54  | 4000  | 0.2152          | 0.1808 |
| 0.355         | 2.86  | 4500  | 0.2179          | 0.1670 |
| 0.3142        | 3.18  | 5000  | 0.1953          | 0.1542 |
| 0.3242        | 3.5   | 5500  | 0.2103          | 0.1526 |
| 0.3016        | 3.82  | 6000  | 0.1911          | 0.1477 |
| 0.2713        | 4.13  | 6500  | 0.1836          | 0.1422 |
| 0.2807        | 4.45  | 7000  | 0.1924          | 0.1447 |
| 0.2929        | 4.77  | 7500  | 0.1848          | 0.1402 |
| 0.2595        | 5.09  | 8000  | 0.1783          | 0.1330 |
| 0.2289        | 5.41  | 8500  | 0.1901          | 0.1313 |
| 0.2567        | 5.72  | 9000  | 0.1784          | 0.1298 |
| 0.2401        | 6.04  | 9500  | 0.1956          | 0.1298 |
| 0.2098        | 6.36  | 10000 | 0.1748          | 0.1277 |
| 0.2246        | 6.68  | 10500 | 0.1777          | 0.1254 |
| 0.2197        | 7.0   | 11000 | 0.1703          | 0.1222 |
| 0.2122        | 7.32  | 11500 | 0.1917          | 0.1221 |
| 0.2746        | 7.63  | 12000 | 0.1769          | 0.1215 |
| 0.2148        | 7.95  | 12500 | 0.1736          | 0.1193 |
| 0.1915        | 8.27  | 13000 | 0.1814          | 0.1161 |
| 0.2462        | 8.59  | 13500 | 0.1748          | 0.1166 |
| 0.1872        | 8.91  | 14000 | 0.1769          | 0.1133 |
| 0.1886        | 9.22  | 14500 | 0.1852          | 0.1143 |
| 0.1789        | 9.54  | 15000 | 0.1696          | 0.1126 |
| 0.1692        | 9.86  | 15500 | 0.1817          | 0.1122 |
| 0.1765        | 10.18 | 16000 | 0.1769          | 0.1093 |
| 0.1699        | 10.5  | 16500 | 0.1604          | 0.1084 |
| 0.1591        | 10.81 | 17000 | 0.1777          | 0.1080 |
| 0.1499        | 11.13 | 17500 | 0.1645          | 0.1074 |
| 0.163         | 11.45 | 18000 | 0.1704          | 0.1065 |
| 0.1597        | 11.77 | 18500 | 0.1576          | 0.1064 |
| 0.1484        | 12.09 | 19000 | 0.1637          | 0.1041 |
| 0.1464        | 12.4  | 19500 | 0.1631          | 0.1047 |
| 0.156         | 12.72 | 20000 | 0.1686          | 0.1029 |
| 0.1625        | 13.04 | 20500 | 0.1648          | 0.1023 |
| 0.1395        | 13.36 | 21000 | 0.1688          | 0.1027 |
| 0.1387        | 13.68 | 21500 | 0.1670          | 0.1013 |
| 0.1434        | 13.99 | 22000 | 0.1677          | 0.1017 |
| 0.1442        | 14.31 | 22500 | 0.1688          | 0.1008 |
| 0.1439        | 14.63 | 23000 | 0.1647          | 0.1004 |
| 0.137         | 14.95 | 23500 | 0.1636          | 0.1006 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0
