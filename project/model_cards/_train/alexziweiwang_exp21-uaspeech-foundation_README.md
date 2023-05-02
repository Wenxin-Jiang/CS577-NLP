---
tags:
- generated_from_trainer
model-index:
- name: exp21-uaspeech-foundation
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# exp21-uaspeech-foundation

This model is a fine-tuned version of [yongjian/wav2vec2-large-a](https://huggingface.co/yongjian/wav2vec2-large-a) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4644
- Wer: 1.2633

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 27.1608       | 0.67  | 500   | 3.0053          | 1.0    |
| 3.2225        | 1.35  | 1000  | 2.8180          | 1.0    |
| 2.7882        | 2.02  | 1500  | 2.5589          | 1.3125 |
| 2.4911        | 2.7   | 2000  | 2.1110          | 1.9129 |
| 2.1921        | 3.37  | 2500  | 1.8404          | 1.8504 |
| 1.833         | 4.04  | 3000  | 1.5873          | 1.8030 |
| 1.51          | 4.72  | 3500  | 1.3015          | 1.6951 |
| 1.2721        | 5.39  | 4000  | 1.2160          | 1.6136 |
| 1.1451        | 6.06  | 4500  | 1.4102          | 1.6212 |
| 0.9631        | 6.74  | 5000  | 1.1730          | 1.5587 |
| 0.9608        | 7.41  | 5500  | 1.4232          | 1.5473 |
| 0.8454        | 8.09  | 6000  | 1.3427          | 1.4830 |
| 0.7377        | 8.76  | 6500  | 1.3691          | 1.4716 |
| 0.6465        | 9.43  | 7000  | 1.4927          | 1.4489 |
| 0.6538        | 10.11 | 7500  | 1.3825          | 1.4072 |
| 0.591         | 10.78 | 8000  | 1.3166          | 1.4186 |
| 0.5476        | 11.46 | 8500  | 1.2636          | 1.3826 |
| 0.515         | 12.13 | 9000  | 1.4861          | 1.4072 |
| 0.5027        | 12.8  | 9500  | 1.7483          | 1.3826 |
| 0.4714        | 13.48 | 10000 | 1.4656          | 1.3598 |
| 0.4506        | 14.15 | 10500 | 1.4430          | 1.3693 |
| 0.3944        | 14.82 | 11000 | 2.0191          | 1.3352 |
| 0.3604        | 15.5  | 11500 | 1.6739          | 1.3428 |
| 0.3533        | 16.17 | 12000 | 1.7428          | 1.3314 |
| 0.3345        | 16.85 | 12500 | 1.6851          | 1.3277 |
| 0.3133        | 17.52 | 13000 | 1.8589          | 1.3106 |
| 0.2772        | 18.19 | 13500 | 2.0114          | 1.2955 |
| 0.2789        | 18.87 | 14000 | 2.0333          | 1.2879 |
| 0.2361        | 19.54 | 14500 | 2.6048          | 1.3030 |
| 0.2406        | 20.22 | 15000 | 2.8444          | 1.2841 |
| 0.2673        | 20.89 | 15500 | 1.9573          | 1.2746 |
| 0.2067        | 21.56 | 16000 | 2.1780          | 1.2936 |
| 0.2281        | 22.24 | 16500 | 2.2629          | 1.2765 |
| 0.1735        | 22.91 | 17000 | 2.2492          | 1.2822 |
| 0.1902        | 23.58 | 17500 | 2.0317          | 1.2803 |
| 0.1659        | 24.26 | 18000 | 2.0658          | 1.2652 |
| 0.1746        | 24.93 | 18500 | 2.2515          | 1.2708 |
| 0.1409        | 25.61 | 19000 | 2.1689          | 1.2595 |
| 0.1461        | 26.28 | 19500 | 2.2441          | 1.2614 |
| 0.1699        | 26.95 | 20000 | 2.1327          | 1.2633 |
| 0.1378        | 27.63 | 20500 | 2.1795          | 1.2670 |
| 0.1108        | 28.3  | 21000 | 2.4057          | 1.2576 |
| 0.1505        | 28.98 | 21500 | 2.4389          | 1.2595 |
| 0.1492        | 29.65 | 22000 | 2.4644          | 1.2633 |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 1.18.3
- Tokenizers 0.13.2
