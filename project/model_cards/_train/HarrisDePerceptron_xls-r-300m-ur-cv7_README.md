---
language:
- ur
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_7_0
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: ''
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_7_0 - UR dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2924
- Wer: 0.7201

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 200.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 11.2783       | 4.17   | 100  | 4.6409          | 1.0    |
| 3.5578        | 8.33   | 200  | 3.1649          | 1.0    |
| 3.1279        | 12.5   | 300  | 3.0335          | 1.0    |
| 2.9944        | 16.67  | 400  | 2.9526          | 0.9983 |
| 2.9275        | 20.83  | 500  | 2.9291          | 1.0009 |
| 2.8077        | 25.0   | 600  | 2.5633          | 0.9895 |
| 2.4438        | 29.17  | 700  | 1.9045          | 0.9564 |
| 1.9659        | 33.33  | 800  | 1.4114          | 0.7960 |
| 1.7092        | 37.5   | 900  | 1.2584          | 0.7637 |
| 1.517         | 41.67  | 1000 | 1.2040          | 0.7507 |
| 1.3966        | 45.83  | 1100 | 1.1273          | 0.7463 |
| 1.3197        | 50.0   | 1200 | 1.1054          | 0.6957 |
| 1.2476        | 54.17  | 1300 | 1.1035          | 0.7001 |
| 1.1796        | 58.33  | 1400 | 1.0890          | 0.7097 |
| 1.1237        | 62.5   | 1500 | 1.0883          | 0.7167 |
| 1.0777        | 66.67  | 1600 | 1.1067          | 0.7219 |
| 1.0051        | 70.83  | 1700 | 1.1115          | 0.7236 |
| 0.9521        | 75.0   | 1800 | 1.0867          | 0.7132 |
| 0.9147        | 79.17  | 1900 | 1.0852          | 0.7210 |
| 0.8798        | 83.33  | 2000 | 1.1411          | 0.7097 |
| 0.8317        | 87.5   | 2100 | 1.1634          | 0.7018 |
| 0.7946        | 91.67  | 2200 | 1.1621          | 0.7201 |
| 0.7594        | 95.83  | 2300 | 1.1482          | 0.7036 |
| 0.729         | 100.0  | 2400 | 1.1493          | 0.7062 |
| 0.7055        | 104.17 | 2500 | 1.1726          | 0.6931 |
| 0.6622        | 108.33 | 2600 | 1.1938          | 0.7001 |
| 0.6583        | 112.5  | 2700 | 1.1832          | 0.7149 |
| 0.6299        | 116.67 | 2800 | 1.1996          | 0.7175 |
| 0.5903        | 120.83 | 2900 | 1.1986          | 0.7132 |
| 0.5816        | 125.0  | 3000 | 1.1909          | 0.7010 |
| 0.5583        | 129.17 | 3100 | 1.2079          | 0.6870 |
| 0.5392        | 133.33 | 3200 | 1.2109          | 0.7228 |
| 0.5412        | 137.5  | 3300 | 1.2353          | 0.7245 |
| 0.5136        | 141.67 | 3400 | 1.2390          | 0.7254 |
| 0.5007        | 145.83 | 3500 | 1.2273          | 0.7123 |
| 0.4883        | 150.0  | 3600 | 1.2773          | 0.7289 |
| 0.4835        | 154.17 | 3700 | 1.2678          | 0.7289 |
| 0.4568        | 158.33 | 3800 | 1.2592          | 0.7350 |
| 0.4525        | 162.5  | 3900 | 1.2705          | 0.7254 |
| 0.4379        | 166.67 | 4000 | 1.2717          | 0.7306 |
| 0.4198        | 170.83 | 4100 | 1.2618          | 0.7219 |
| 0.4216        | 175.0  | 4200 | 1.2909          | 0.7158 |
| 0.4305        | 179.17 | 4300 | 1.2808          | 0.7167 |
| 0.399         | 183.33 | 4400 | 1.2750          | 0.7193 |
| 0.3937        | 187.5  | 4500 | 1.2719          | 0.7149 |
| 0.3905        | 191.67 | 4600 | 1.2816          | 0.7158 |
| 0.3892        | 195.83 | 4700 | 1.2951          | 0.7210 |
| 0.3932        | 200.0  | 4800 | 1.2924          | 0.7201 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0
