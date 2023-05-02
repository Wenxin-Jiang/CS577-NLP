---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-small-gec-new_data
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-gec-new_data

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4766
- Rouge1: 75.2888
- Rouge2: 62.2647
- Rougel: 75.0714
- Rougelsum: 75.0665
- Gen Len: 17.3713

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 1.0361        | 0.2   | 50   | 0.8441          | 33.973  | 25.3214 | 33.6752 | 33.6214   | 17.8812 |
| 0.9318        | 0.4   | 100  | 0.7763          | 39.7001 | 30.2026 | 39.4182 | 39.4068   | 17.8703 |
| 0.8131        | 0.6   | 150  | 0.7200          | 48.3335 | 37.3238 | 47.9675 | 47.9161   | 17.7565 |
| 0.7757        | 0.8   | 200  | 0.6869          | 56.1066 | 43.9612 | 55.7915 | 55.7617   | 17.6756 |
| 0.7377        | 1.0   | 250  | 0.6532          | 62.602  | 49.6693 | 62.3543 | 62.3558   | 17.5729 |
| 0.7208        | 1.2   | 300  | 0.6236          | 67.022  | 53.6375 | 66.6774 | 66.7084   | 17.52   |
| 0.6936        | 1.39  | 350  | 0.6001          | 69.1363 | 55.5412 | 68.8118 | 68.8147   | 17.48   |
| 0.6537        | 1.59  | 400  | 0.5802          | 70.7095 | 57.095  | 70.4215 | 70.4339   | 17.4481 |
| 0.6509        | 1.79  | 450  | 0.5648          | 71.9193 | 58.2398 | 71.6452 | 71.6588   | 17.4261 |
| 0.6417        | 1.99  | 500  | 0.5513          | 72.5913 | 58.9961 | 72.344  | 72.3608   | 17.4072 |
| 0.6291        | 2.19  | 550  | 0.5371          | 73.0143 | 59.5651 | 72.7976 | 72.7995   | 17.3922 |
| 0.5976        | 2.39  | 600  | 0.5269          | 73.5372 | 60.1145 | 73.3427 | 73.3373   | 17.3743 |
| 0.5677        | 2.59  | 650  | 0.5182          | 73.9687 | 60.5451 | 73.7523 | 73.7587   | 17.3503 |
| 0.6073        | 2.79  | 700  | 0.5112          | 74.1167 | 60.7119 | 73.9078 | 73.9058   | 17.3543 |
| 0.5904        | 2.99  | 750  | 0.5050          | 74.3731 | 61.0562 | 74.1668 | 74.1611   | 17.3513 |
| 0.5848        | 3.19  | 800  | 0.4984          | 74.5208 | 61.2305 | 74.3101 | 74.31     | 17.3623 |
| 0.5627        | 3.39  | 850  | 0.4941          | 74.7645 | 61.5633 | 74.5559 | 74.5451   | 17.3633 |
| 0.5649        | 3.59  | 900  | 0.4898          | 74.9032 | 61.8229 | 74.6977 | 74.682    | 17.3673 |
| 0.5524        | 3.78  | 950  | 0.4871          | 74.9793 | 61.8885 | 74.7644 | 74.7611   | 17.3613 |
| 0.5596        | 3.98  | 1000 | 0.4837          | 75.1194 | 62.0917 | 74.8961 | 74.8987   | 17.3723 |
| 0.5627        | 4.18  | 1050 | 0.4809          | 75.2394 | 62.2355 | 75.0183 | 75.0197   | 17.3683 |
| 0.5551        | 4.38  | 1100 | 0.4790          | 75.2504 | 62.24   | 75.0235 | 75.0216   | 17.3683 |
| 0.5443        | 4.58  | 1150 | 0.4777          | 75.2608 | 62.2536 | 75.0394 | 75.0403   | 17.3723 |
| 0.5414        | 4.78  | 1200 | 0.4769          | 75.2812 | 62.264  | 75.0614 | 75.058    | 17.3723 |
| 0.5602        | 4.98  | 1250 | 0.4766          | 75.2888 | 62.2647 | 75.0714 | 75.0665   | 17.3713 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2