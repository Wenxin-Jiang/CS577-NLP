---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-3front-1body-3rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-3front-1body-3rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4427
- Wer: 0.1709
- Mer: 0.1651
- Wil: 0.2519
- Wip: 0.7481
- Hits: 55802
- Substitutions: 6391
- Deletions: 2394
- Insertions: 2252
- Cer: 0.1337

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
| 0.628         | 1.0   | 1457  | 0.4785          | 0.2008 | 0.1912 | 0.2803 | 0.7197 | 54855 | 6650          | 3082      | 3234       | 0.1735 |
| 0.5271        | 2.0   | 2914  | 0.4292          | 0.1779 | 0.1718 | 0.2602 | 0.7398 | 55387 | 6527          | 2673      | 2293       | 0.1469 |
| 0.4724        | 3.0   | 4371  | 0.4222          | 0.1719 | 0.1664 | 0.2530 | 0.7470 | 55610 | 6365          | 2612      | 2123       | 0.1353 |
| 0.4125        | 4.0   | 5828  | 0.4174          | 0.1707 | 0.1653 | 0.2512 | 0.7488 | 55694 | 6304          | 2589      | 2135       | 0.1342 |
| 0.3646        | 5.0   | 7285  | 0.4218          | 0.1712 | 0.1655 | 0.2521 | 0.7479 | 55756 | 6373          | 2458      | 2224       | 0.1339 |
| 0.3232        | 6.0   | 8742  | 0.4253          | 0.1695 | 0.1642 | 0.2505 | 0.7495 | 55726 | 6340          | 2521      | 2087       | 0.1333 |
| 0.3583        | 7.0   | 10199 | 0.4303          | 0.1699 | 0.1645 | 0.2514 | 0.7486 | 55733 | 6393          | 2461      | 2120       | 0.1338 |
| 0.2894        | 8.0   | 11656 | 0.4355          | 0.1699 | 0.1643 | 0.2508 | 0.7492 | 55827 | 6371          | 2389      | 2215       | 0.1325 |
| 0.2825        | 9.0   | 13113 | 0.4399          | 0.1705 | 0.1648 | 0.2518 | 0.7482 | 55785 | 6409          | 2393      | 2207       | 0.1334 |
| 0.2901        | 10.0  | 14570 | 0.4427          | 0.1709 | 0.1651 | 0.2519 | 0.7481 | 55802 | 6391          | 2394      | 2252       | 0.1337 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
