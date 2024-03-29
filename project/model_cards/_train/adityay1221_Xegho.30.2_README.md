---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: Xegho.30.2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Xegho.30.2

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1632
- Bleu: 91.1608

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 121
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| No log        | 0.6   | 100  | 1.4767          | 23.2970 |
| No log        | 1.19  | 200  | 1.0102          | 34.8884 |
| No log        | 1.79  | 300  | 0.7680          | 39.9415 |
| No log        | 2.38  | 400  | 0.6129          | 42.4210 |
| 1.2252        | 2.98  | 500  | 0.4962          | 46.5901 |
| 1.2252        | 3.57  | 600  | 0.4293          | 48.9165 |
| 1.2252        | 4.17  | 700  | 0.3698          | 50.4146 |
| 1.2252        | 4.76  | 800  | 0.3194          | 52.4519 |
| 1.2252        | 5.36  | 900  | 0.2836          | 53.0005 |
| 0.463         | 5.95  | 1000 | 0.2635          | 55.5264 |
| 0.463         | 6.55  | 1100 | 0.2444          | 57.7553 |
| 0.463         | 7.14  | 1200 | 0.2262          | 60.8152 |
| 0.463         | 7.74  | 1300 | 0.2205          | 60.3349 |
| 0.463         | 8.33  | 1400 | 0.2082          | 62.5781 |
| 0.297         | 8.93  | 1500 | 0.2045          | 62.9341 |
| 0.297         | 9.52  | 1600 | 0.1969          | 63.9225 |
| 0.297         | 10.12 | 1700 | 0.1939          | 63.9559 |
| 0.297         | 10.71 | 1800 | 0.1842          | 66.0123 |
| 0.297         | 11.31 | 1900 | 0.1836          | 65.7767 |
| 0.2403        | 11.9  | 2000 | 0.1807          | 65.1204 |
| 0.2403        | 12.5  | 2100 | 0.1778          | 65.5556 |
| 0.2403        | 13.1  | 2200 | 0.1753          | 66.2715 |
| 0.2403        | 13.69 | 2300 | 0.1728          | 67.0917 |
| 0.2403        | 14.29 | 2400 | 0.1716          | 67.2965 |
| 0.1976        | 14.88 | 2500 | 0.1719          | 66.5856 |
| 0.1976        | 15.48 | 2600 | 0.1706          | 66.7707 |
| 0.1976        | 16.07 | 2700 | 0.1698          | 66.8323 |
| 0.1976        | 16.67 | 2800 | 0.1705          | 66.8579 |
| 0.1976        | 17.26 | 2900 | 0.1663          | 67.3175 |
| 0.1747        | 17.86 | 3000 | 0.1671          | 68.2097 |
| 0.1747        | 18.45 | 3100 | 0.1681          | 68.1515 |
| 0.1747        | 19.05 | 3200 | 0.1650          | 68.6221 |
| 0.1747        | 19.64 | 3300 | 0.1643          | 68.6828 |
| 0.1747        | 20.24 | 3400 | 0.1662          | 68.9329 |
| 0.1626        | 20.83 | 3500 | 0.1644          | 68.9651 |
| 0.1626        | 21.43 | 3600 | 0.1660          | 68.6685 |
| 0.1626        | 22.02 | 3700 | 0.1640          | 68.7471 |
| 0.1626        | 22.62 | 3800 | 0.1630          | 68.6685 |
| 0.1626        | 23.21 | 3900 | 0.1637          | 68.6835 |
| 0.1437        | 23.81 | 4000 | 0.1632          | 68.5208 |
| 0.1437        | 24.4  | 4100 | 0.1640          | 68.5059 |
| 0.1437        | 25.0  | 4200 | 0.1645          | 68.5059 |
| 0.1437        | 25.6  | 4300 | 0.1639          | 68.5059 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0a0+17540c5
- Datasets 2.1.0
- Tokenizers 0.12.1
