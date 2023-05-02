---
language:
- ur
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
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

This model is a fine-tuned version of [DrishtiSharma/wav2vec2-large-xls-r-300m-hi-d3](https://huggingface.co/DrishtiSharma/wav2vec2-large-xls-r-300m-hi-d3) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - UR dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5443
- Wer: 0.7030

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.000388
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 750
- num_epochs: 100.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 10.7052       | 1.96  | 100  | 3.4683          | 1.0    |
| 3.2395        | 3.92  | 200  | 3.1489          | 1.0    |
| 2.9951        | 5.88  | 300  | 2.9823          | 1.0007 |
| 2.3574        | 7.84  | 400  | 1.2614          | 0.7598 |
| 1.7287        | 9.8   | 500  | 1.1817          | 0.7421 |
| 1.6144        | 11.76 | 600  | 1.1315          | 0.7321 |
| 1.5598        | 13.73 | 700  | 1.2322          | 0.7550 |
| 1.5418        | 15.69 | 800  | 1.2721          | 0.7819 |
| 1.4578        | 17.65 | 900  | 1.1710          | 0.7531 |
| 1.4311        | 19.61 | 1000 | 1.2042          | 0.7491 |
| 1.3483        | 21.57 | 1100 | 1.1702          | 0.7465 |
| 1.3078        | 23.53 | 1200 | 1.1963          | 0.7421 |
| 1.2576        | 25.49 | 1300 | 1.1501          | 0.7280 |
| 1.2173        | 27.45 | 1400 | 1.2526          | 0.7299 |
| 1.2217        | 29.41 | 1500 | 1.2479          | 0.7310 |
| 1.1536        | 31.37 | 1600 | 1.2567          | 0.7432 |
| 1.0939        | 33.33 | 1700 | 1.2801          | 0.7247 |
| 1.0745        | 35.29 | 1800 | 1.2340          | 0.7151 |
| 1.0454        | 37.25 | 1900 | 1.2372          | 0.7151 |
| 1.0101        | 39.22 | 2000 | 1.2461          | 0.7376 |
| 0.9833        | 41.18 | 2100 | 1.2553          | 0.7269 |
| 0.9314        | 43.14 | 2200 | 1.2372          | 0.7015 |
| 0.9147        | 45.1  | 2300 | 1.3035          | 0.7358 |
| 0.8758        | 47.06 | 2400 | 1.2598          | 0.7092 |
| 0.8356        | 49.02 | 2500 | 1.2557          | 0.7144 |
| 0.8105        | 50.98 | 2600 | 1.2619          | 0.7236 |
| 0.7947        | 52.94 | 2700 | 1.3994          | 0.7491 |
| 0.7623        | 54.9  | 2800 | 1.2932          | 0.7133 |
| 0.7282        | 56.86 | 2900 | 1.2799          | 0.7089 |
| 0.7108        | 58.82 | 3000 | 1.3615          | 0.7148 |
| 0.6896        | 60.78 | 3100 | 1.3129          | 0.7041 |
| 0.6496        | 62.75 | 3200 | 1.4050          | 0.6934 |
| 0.6075        | 64.71 | 3300 | 1.3571          | 0.7026 |
| 0.6242        | 66.67 | 3400 | 1.3369          | 0.7063 |
| 0.5865        | 68.63 | 3500 | 1.4368          | 0.7140 |
| 0.5721        | 70.59 | 3600 | 1.4224          | 0.7066 |
| 0.5475        | 72.55 | 3700 | 1.4798          | 0.7118 |
| 0.5086        | 74.51 | 3800 | 1.5107          | 0.7232 |
| 0.4958        | 76.47 | 3900 | 1.4849          | 0.7089 |
| 0.5046        | 78.43 | 4000 | 1.4451          | 0.7114 |
| 0.4694        | 80.39 | 4100 | 1.4674          | 0.7089 |
| 0.4386        | 82.35 | 4200 | 1.5245          | 0.7103 |
| 0.4516        | 84.31 | 4300 | 1.5032          | 0.7103 |
| 0.4113        | 86.27 | 4400 | 1.5246          | 0.7196 |
| 0.3972        | 88.24 | 4500 | 1.5318          | 0.7114 |
| 0.4006        | 90.2  | 4600 | 1.5543          | 0.6982 |
| 0.4014        | 92.16 | 4700 | 1.5442          | 0.7048 |
| 0.3672        | 94.12 | 4800 | 1.5542          | 0.7137 |
| 0.3666        | 96.08 | 4900 | 1.5414          | 0.7018 |
| 0.3574        | 98.04 | 5000 | 1.5465          | 0.7059 |
| 0.3428        | 100.0 | 5100 | 1.5443          | 0.7030 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0
