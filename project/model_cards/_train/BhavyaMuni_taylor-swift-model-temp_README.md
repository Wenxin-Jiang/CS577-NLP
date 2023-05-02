---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: taylor-swift-model-temp
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# taylor-swift-model-temp

This model is a fine-tuned version of [distilgpt2](https://huggingface.co/distilgpt2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.1118

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 4.0072        | 1.0   | 58   | 3.7794          |
| 3.8685        | 2.0   | 116  | 3.6857          |
| 3.8123        | 3.0   | 174  | 3.6220          |
| 3.7141        | 4.0   | 232  | 3.5796          |
| 3.3674        | 5.0   | 290  | 3.5402          |
| 3.556         | 6.0   | 348  | 3.5092          |
| 3.442         | 7.0   | 406  | 3.4829          |
| 3.5147        | 8.0   | 464  | 3.4609          |
| 3.3591        | 9.0   | 522  | 3.4289          |
| 3.3258        | 10.0  | 580  | 3.4135          |
| 3.2393        | 11.0  | 638  | 3.3918          |
| 3.2989        | 12.0  | 696  | 3.3756          |
| 3.2535        | 13.0  | 754  | 3.3557          |
| 3.1144        | 14.0  | 812  | 3.3352          |
| 2.9332        | 15.0  | 870  | 3.3305          |
| 3.0371        | 16.0  | 928  | 3.3078          |
| 3.0357        | 17.0  | 986  | 3.2889          |
| 2.8728        | 18.0  | 1044 | 3.2851          |
| 2.9121        | 19.0  | 1102 | 3.2688          |
| 2.9804        | 20.0  | 1160 | 3.2562          |
| 2.855         | 21.0  | 1218 | 3.2485          |
| 2.7546        | 22.0  | 1276 | 3.2275          |
| 2.9248        | 23.0  | 1334 | 3.2233          |
| 2.9627        | 24.0  | 1392 | 3.2113          |
| 2.891         | 25.0  | 1450 | 3.1965          |
| 2.7106        | 26.0  | 1508 | 3.1925          |
| 2.8863        | 27.0  | 1566 | 3.1836          |
| 2.8311        | 28.0  | 1624 | 3.1869          |
| 2.6953        | 29.0  | 1682 | 3.1769          |
| 2.7916        | 30.0  | 1740 | 3.1717          |
| 2.7262        | 31.0  | 1798 | 3.1609          |
| 2.6203        | 32.0  | 1856 | 3.1564          |
| 2.7066        | 33.0  | 1914 | 3.1492          |
| 2.3818        | 34.0  | 1972 | 3.1475          |
| 2.7237        | 35.0  | 2030 | 3.1412          |
| 2.4593        | 36.0  | 2088 | 3.1372          |
| 2.5471        | 37.0  | 2146 | 3.1298          |
| 2.6026        | 38.0  | 2204 | 3.1324          |
| 2.5049        | 39.0  | 2262 | 3.1285          |
| 2.5509        | 40.0  | 2320 | 3.1262          |
| 2.7736        | 41.0  | 2378 | 3.1142          |
| 2.7144        | 42.0  | 2436 | 3.1159          |
| 2.5972        | 43.0  | 2494 | 3.1145          |
| 2.5897        | 44.0  | 2552 | 3.1142          |
| 2.4131        | 45.0  | 2610 | 3.1152          |
| 2.5602        | 46.0  | 2668 | 3.1130          |
| 2.4986        | 47.0  | 2726 | 3.1123          |
| 2.5507        | 48.0  | 2784 | 3.1108          |
| 2.4885        | 49.0  | 2842 | 3.1124          |
| 2.4204        | 50.0  | 2900 | 3.1118          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
