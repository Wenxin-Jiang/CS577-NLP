---
license: cc0-1.0
tags:
- automatic-speech-recognition
- NbAiLab/NPSC
- generated_from_trainer
- robust-speech-event
datasets:
- NbAiLab/NPSC
model-index:
- name: wav2vec2-large-voxrex-npsc
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-voxrex-npsc

This model is a fine-tuned version of [KBLab/wav2vec2-large-voxrex](https://huggingface.co/KBLab/wav2vec2-large-voxrex) on the NBAILAB/NPSC - 16K_MP3 dataset.
It achieves the following results on the evaluation set:
- Loss: nan
- Wer: 1.0

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
| 2.9728        | 0.32  | 500   | 2.9449          | 1.0    |
| 2.5099        | 0.64  | 1000  | 1.8492          | 0.9910 |
| 0.7872        | 0.97  | 1500  | 0.4467          | 0.3774 |
| 0.5993        | 1.29  | 2000  | 0.3181          | 0.2819 |
| 0.5134        | 1.61  | 2500  | 0.2638          | 0.2401 |
| 0.4544        | 1.93  | 3000  | 0.2287          | 0.2091 |
| 0.4085        | 2.26  | 3500  | 0.2153          | 0.1918 |
| 0.3921        | 2.58  | 4000  | 0.2004          | 0.1804 |
| 0.4613        | 2.9   | 4500  | 0.1905          | 0.1732 |
| 0.3402        | 3.22  | 5000  | 0.1778          | 0.1659 |
| 0.3258        | 3.55  | 5500  | 0.1732          | 0.1571 |
| 0.3044        | 3.87  | 6000  | 0.1677          | 0.1497 |
| 0.2914        | 4.19  | 6500  | 0.1597          | 0.1420 |
| 0.278         | 4.51  | 7000  | 0.1574          | 0.1386 |
| 0.2858        | 4.84  | 7500  | 0.1552          | 0.1300 |
| 0.2585        | 5.16  | 8000  | 0.1523          | 0.1276 |
| 0.2827        | 5.48  | 8500  | 0.1448          | 0.1265 |
| 0.3365        | 5.8   | 9000  | 0.1411          | 0.1232 |
| 0.2488        | 6.13  | 9500  | 0.1456          | 0.1195 |
| 0.2406        | 6.45  | 10000 | 0.1414          | 0.1194 |
| 0.2488        | 6.77  | 10500 | 0.1393          | 0.1173 |
| 0.3084        | 7.09  | 11000 | 0.1379          | 0.1164 |
| 0.2365        | 7.41  | 11500 | 0.1387          | 0.1165 |
| 0.2217        | 7.74  | 12000 | 0.1381          | 0.1132 |
| 0.2381        | 8.06  | 12500 | 0.1360          | 0.1126 |
| 0.2329        | 8.38  | 13000 | 0.1357          | 0.1124 |
| 0.2103        | 8.7   | 13500 | 0.1335          | 0.1087 |
| 0.2366        | 9.03  | 14000 | 0.1388          | 0.1105 |
| 0.2289        | 9.35  | 14500 | 0.1383          | 0.1098 |
| 0.2486        | 9.67  | 15000 | 0.1386          | 0.1087 |
| **0.2772**        | **9.99**  | **15500** | **0.1598**          | **0.1093** |
| 0.2728        | 10.32 | 16000 | 0.1814          | 0.1110 |
| 0.3437        | 10.64 | 16500 | 0.2505          | 0.1124 |
| 0.431         | 10.96 | 17000 | 0.2828          | 0.1143 |
| 0.3929        | 11.28 | 17500 | 0.2977          | 0.1149 |
| 0.4396        | 11.61 | 18000 | 0.3198          | 0.1170 |
| 0.59          | 11.93 | 18500 | 0.4158          | 0.1315 |
| 0.7813        | 12.25 | 19000 | 0.6123          | 0.2208 |
| 0.9345        | 12.57 | 19500 | 0.6815          | 0.2885 |
| 0.998         | 12.89 | 20000 | 0.7587          | 0.1991 |
| 1.0493        | 13.22 | 20500 | 0.7583          | 0.1996 |
| 1.438         | 13.54 | 21000 | nan             | 1.0    |
| 0.0           | 13.86 | 21500 | nan             | 1.0    |
| 0.0           | 14.18 | 22000 | nan             | 1.0    |
| 0.0           | 14.51 | 22500 | nan             | 1.0    |
| 0.0           | 14.83 | 23000 | nan             | 1.0    |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu113
- Datasets 1.18.3.dev0
- Tokenizers 0.11.0
