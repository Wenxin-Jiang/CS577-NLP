---
tags:
- generated_from_trainer
model-index:
- name: uaspeech-foundation-fintuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# uaspeech-foundation-fintuned

This model is a fine-tuned version of [yongjian/wav2vec2-large-a](https://huggingface.co/yongjian/wav2vec2-large-a) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.5324
- Wer: 1.2855

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
| 41.2984       | 0.7   | 500   | 2.8954          | 1.0    |
| 3.0227        | 1.4   | 1000  | 2.8232          | 1.0042 |
| 2.8283        | 2.11  | 1500  | 2.6291          | 1.0309 |
| 2.5552        | 2.81  | 2000  | 2.2593          | 1.9170 |
| 2.1714        | 3.51  | 2500  | 1.9586          | 1.9142 |
| 1.8537        | 4.21  | 3000  | 1.5725          | 1.8579 |
| 1.6087        | 4.92  | 3500  | 1.2772          | 1.7426 |
| 1.3108        | 5.62  | 4000  | 1.2792          | 1.6751 |
| 1.1652        | 6.32  | 4500  | 1.4565          | 1.6174 |
| 1.0113        | 7.02  | 5000  | 1.1906          | 1.5626 |
| 0.925         | 7.72  | 5500  | 1.4491          | 1.5260 |
| 0.8183        | 8.43  | 6000  | 1.3712          | 1.5387 |
| 0.7118        | 9.13  | 6500  | 1.4713          | 1.4866 |
| 0.6959        | 9.83  | 7000  | 1.3336          | 1.4318 |
| 0.6146        | 10.53 | 7500  | 1.3690          | 1.4177 |
| 0.5655        | 11.24 | 8000  | 1.3789          | 1.4135 |
| 0.4969        | 11.94 | 8500  | 1.5476          | 1.3966 |
| 0.4705        | 12.64 | 9000  | 1.9062          | 1.3797 |
| 0.4387        | 13.34 | 9500  | 1.2711          | 1.3924 |
| 0.4115        | 14.04 | 10000 | 1.6318          | 1.3769 |
| 0.3695        | 14.75 | 10500 | 1.5119          | 1.3755 |
| 0.377         | 15.45 | 11000 | 1.6637          | 1.3812 |
| 0.3788        | 16.15 | 11500 | 1.6636          | 1.3699 |
| 0.3396        | 16.85 | 12000 | 1.6572          | 1.3418 |
| 0.3047        | 17.56 | 12500 | 1.4740          | 1.3361 |
| 0.2804        | 18.26 | 13000 | 2.0885          | 1.3249 |
| 0.2995        | 18.96 | 13500 | 1.9536          | 1.3235 |
| 0.2628        | 19.66 | 14000 | 1.7736          | 1.3179 |
| 0.2703        | 20.37 | 14500 | 2.0018          | 1.3291 |
| 0.2335        | 21.07 | 15000 | 1.7962          | 1.3221 |
| 0.2068        | 21.77 | 15500 | 2.3187          | 1.3136 |
| 0.2311        | 22.47 | 16000 | 2.4853          | 1.3291 |
| 0.2491        | 23.17 | 16500 | 2.1901          | 1.3024 |
| 0.1836        | 23.88 | 17000 | 2.4344          | 1.2911 |
| 0.1823        | 24.58 | 17500 | 2.3705          | 1.3066 |
| 0.1575        | 25.28 | 18000 | 2.1864          | 1.2897 |
| 0.1451        | 25.98 | 18500 | 2.4216          | 1.2883 |
| 0.1502        | 26.69 | 19000 | 2.1780          | 1.2855 |
| 0.1392        | 27.39 | 19500 | 2.4009          | 1.2925 |
| 0.1609        | 28.09 | 20000 | 2.4250          | 1.2982 |
| 0.1066        | 28.79 | 20500 | 2.4433          | 1.2897 |
| 0.1514        | 29.49 | 21000 | 2.5063          | 1.2855 |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 1.18.3
- Tokenizers 0.13.2
