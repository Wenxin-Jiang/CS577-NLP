---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: Spoof_detection
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Spoof_detection

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7448
- Wer: 0.1090

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
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 95.9046       | 0.66  | 500   | 992.2993        | 0.6180 |
| 14.0322       | 1.33  | 1000  | 1.8873          | 0.1090 |
| 1.8659        | 1.99  | 1500  | 1.7827          | 0.1090 |
| 1.851         | 2.65  | 2000  | 1.8489          | 0.1090 |
| 1.8218        | 3.32  | 2500  | 1.8943          | 0.1090 |
| 1.8108        | 3.98  | 3000  | 1.9250          | 0.1090 |
| 1.8228        | 4.64  | 3500  | 1.7555          | 0.1090 |
| 1.832         | 5.31  | 4000  | 1.7837          | 0.1090 |
| 1.8403        | 5.97  | 4500  | 1.6644          | 0.1090 |
| 1.8292        | 6.63  | 5000  | 1.6906          | 0.1090 |
| 1.8223        | 7.29  | 5500  | 1.6966          | 0.1090 |
| 1.8007        | 7.96  | 6000  | 1.6951          | 0.1090 |
| 1.7986        | 8.62  | 6500  | 1.7436          | 0.1090 |
| 1.7933        | 9.28  | 7000  | 1.8169          | 0.1090 |
| 1.7861        | 9.95  | 7500  | 1.7209          | 0.1090 |
| 1.7843        | 10.61 | 8000  | 1.9379          | 0.1090 |
| 1.7743        | 11.27 | 8500  | 1.9834          | 0.1090 |
| 1.7721        | 11.94 | 9000  | 1.9279          | 0.1090 |
| 1.7719        | 12.6  | 9500  | 1.8187          | 0.1090 |
| 1.7616        | 13.26 | 10000 | 1.7804          | 0.1090 |
| 1.7638        | 13.93 | 10500 | 1.7884          | 0.1090 |
| 1.7651        | 14.59 | 11000 | 1.7476          | 0.1090 |
| 1.7603        | 15.25 | 11500 | 1.7570          | 0.1090 |
| 1.7543        | 15.92 | 12000 | 1.7356          | 0.1090 |
| 1.7556        | 16.58 | 12500 | 1.7140          | 0.1090 |
| 1.751         | 17.24 | 13000 | 1.7453          | 0.1090 |
| 1.75          | 17.9  | 13500 | 1.7648          | 0.1090 |
| 1.7492        | 18.57 | 14000 | 1.7338          | 0.1090 |
| 1.7484        | 19.23 | 14500 | 1.7093          | 0.1090 |
| 1.7461        | 19.89 | 15000 | 1.7393          | 0.1090 |
| 1.7429        | 20.56 | 15500 | 1.7605          | 0.1090 |
| 1.7446        | 21.22 | 16000 | 1.7782          | 0.1090 |
| 1.7435        | 21.88 | 16500 | 1.6749          | 0.1090 |
| 1.7392        | 22.55 | 17000 | 1.7468          | 0.1090 |
| 1.741         | 23.21 | 17500 | 1.7406          | 0.1090 |
| 1.7394        | 23.87 | 18000 | 1.7787          | 0.1090 |
| 1.739         | 24.54 | 18500 | 1.7969          | 0.1090 |
| 1.7341        | 25.2  | 19000 | 1.7490          | 0.1090 |
| 1.7371        | 25.86 | 19500 | 1.7783          | 0.1090 |
| 1.735         | 26.53 | 20000 | 1.7540          | 0.1090 |
| 1.7353        | 27.19 | 20500 | 1.7735          | 0.1090 |
| 1.7331        | 27.85 | 21000 | 1.7188          | 0.1090 |
| 1.7308        | 28.51 | 21500 | 1.7349          | 0.1090 |
| 1.7341        | 29.18 | 22000 | 1.7531          | 0.1090 |
| 1.7305        | 29.84 | 22500 | 1.7448          | 0.1090 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu102
- Datasets 1.16.1
- Tokenizers 0.12.1
