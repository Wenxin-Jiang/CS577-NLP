---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-4front-1body-4rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-4front-1body-4rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4406
- Wer: 0.1708
- Mer: 0.1650
- Wil: 0.2510
- Wip: 0.7490
- Hits: 55830
- Substitutions: 6334
- Deletions: 2423
- Insertions: 2273
- Cer: 0.1334

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    | Mer    | Wil    | Wip    | Hits  | Substitutions | Deletions | Insertions | Cer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:------:|:------:|:-----:|:-------------:|:---------:|:----------:|:------:|
| 0.6266        | 1.0   | 1457  | 0.4764          | 0.2167 | 0.2030 | 0.2919 | 0.7081 | 54977 | 6723          | 2887      | 4389       | 0.1978 |
| 0.512         | 2.0   | 2914  | 0.4281          | 0.1787 | 0.1727 | 0.2600 | 0.7400 | 55299 | 6432          | 2856      | 2253       | 0.1408 |
| 0.4636        | 3.0   | 4371  | 0.4205          | 0.1775 | 0.1708 | 0.2582 | 0.7418 | 55665 | 6466          | 2456      | 2540       | 0.1383 |
| 0.4055        | 4.0   | 5828  | 0.4158          | 0.1721 | 0.1663 | 0.2529 | 0.7471 | 55724 | 6376          | 2487      | 2250       | 0.1344 |
| 0.356         | 5.0   | 7285  | 0.4195          | 0.1711 | 0.1654 | 0.2520 | 0.7480 | 55769 | 6376          | 2442      | 2235       | 0.1338 |
| 0.3273        | 6.0   | 8742  | 0.4228          | 0.1700 | 0.1644 | 0.2506 | 0.7494 | 55792 | 6333          | 2462      | 2183       | 0.1330 |
| 0.3586        | 7.0   | 10199 | 0.4288          | 0.1702 | 0.1645 | 0.2506 | 0.7494 | 55814 | 6331          | 2442      | 2219       | 0.1326 |
| 0.2836        | 8.0   | 11656 | 0.4339          | 0.1710 | 0.1651 | 0.2515 | 0.7485 | 55833 | 6359          | 2395      | 2290       | 0.1334 |
| 0.285         | 9.0   | 13113 | 0.4370          | 0.1708 | 0.1649 | 0.2509 | 0.7491 | 55854 | 6330          | 2403      | 2297       | 0.1333 |
| 0.285         | 10.0  | 14570 | 0.4406          | 0.1708 | 0.1650 | 0.2510 | 0.7490 | 55830 | 6334          | 2423      | 2273       | 0.1334 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
