---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-base-finetuned-qg-context-dataset-2-hard-medium
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-finetuned-qg-context-dataset-2-hard-medium

This model is a fine-tuned version of [Deigant/t5-base-finetuned-qg-context-dataset-2](https://huggingface.co/Deigant/t5-base-finetuned-qg-context-dataset-2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1877
- Rouge1: 27.9067
- Rouge2: 6.8779
- Rougel: 24.6502
- Rougelsum: 24.7749

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| No log        | 1.0   | 73   | 2.1134          | 27.571  | 8.3183  | 25.3973 | 25.2743   |
| No log        | 2.0   | 146  | 2.0800          | 28.4972 | 9.7451  | 26.9093 | 26.7337   |
| No log        | 3.0   | 219  | 2.0406          | 21.4309 | 5.817   | 19.4819 | 19.8555   |
| No log        | 4.0   | 292  | 2.0391          | 27.2786 | 8.283   | 24.3314 | 24.3751   |
| No log        | 5.0   | 365  | 2.0367          | 26.3524 | 7.6263  | 23.9034 | 23.8929   |
| No log        | 6.0   | 438  | 2.0270          | 26.3718 | 6.7074  | 22.995  | 23.0177   |
| 1.3439        | 7.0   | 511  | 2.0106          | 27.8601 | 10.5485 | 26.8103 | 26.4962   |
| 1.3439        | 8.0   | 584  | 2.0292          | 27.1811 | 7.1941  | 23.9117 | 24.0093   |
| 1.3439        | 9.0   | 657  | 2.0462          | 25.6595 | 8.3529  | 23.0955 | 23.1946   |
| 1.3439        | 10.0  | 730  | 2.0600          | 27.1996 | 9.0098  | 25.7921 | 25.8295   |
| 1.3439        | 11.0  | 803  | 2.0754          | 25.3094 | 7.6857  | 23.5524 | 23.6875   |
| 1.3439        | 12.0  | 876  | 2.0532          | 27.2136 | 9.0147  | 24.7405 | 24.8211   |
| 1.3439        | 13.0  | 949  | 2.0742          | 26.298  | 8.6826  | 24.6878 | 24.9118   |
| 0.8957        | 14.0  | 1022 | 2.0975          | 22.9575 | 4.2021  | 20.6208 | 20.6539   |
| 0.8957        | 15.0  | 1095 | 2.0941          | 26.778  | 7.1756  | 24.4053 | 24.4951   |
| 0.8957        | 16.0  | 1168 | 2.1025          | 28.9102 | 10.5549 | 25.912  | 25.9433   |
| 0.8957        | 17.0  | 1241 | 2.1265          | 27.8301 | 9.7377  | 25.3236 | 25.3889   |
| 0.8957        | 18.0  | 1314 | 2.1403          | 26.1619 | 7.8019  | 23.5346 | 23.351    |
| 0.8957        | 19.0  | 1387 | 2.1396          | 26.664  | 6.8261  | 24.2991 | 24.328    |
| 0.8957        | 20.0  | 1460 | 2.1481          | 29.8898 | 9.8211  | 27.0922 | 27.2485   |
| 0.69          | 21.0  | 1533 | 2.1466          | 26.3418 | 5.7845  | 24.0772 | 24.3122   |
| 0.69          | 22.0  | 1606 | 2.1559          | 27.5789 | 7.7653  | 25.9896 | 25.8088   |
| 0.69          | 23.0  | 1679 | 2.1624          | 27.9455 | 7.4094  | 25.3163 | 25.3905   |
| 0.69          | 24.0  | 1752 | 2.1633          | 27.5236 | 8.1967  | 24.9498 | 24.974    |
| 0.69          | 25.0  | 1825 | 2.1698          | 26.899  | 6.4382  | 24.2075 | 24.1523   |
| 0.69          | 26.0  | 1898 | 2.1745          | 28.7721 | 8.872   | 24.8299 | 24.9028   |
| 0.69          | 27.0  | 1971 | 2.1818          | 25.8046 | 6.0655  | 23.156  | 23.1971   |
| 0.5965        | 28.0  | 2044 | 2.1854          | 25.4431 | 4.6566  | 22.2794 | 22.4561   |
| 0.5965        | 29.0  | 2117 | 2.1858          | 24.7881 | 6.4357  | 22.8869 | 22.8331   |
| 0.5965        | 30.0  | 2190 | 2.1877          | 27.9067 | 6.8779  | 24.6502 | 24.7749   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
