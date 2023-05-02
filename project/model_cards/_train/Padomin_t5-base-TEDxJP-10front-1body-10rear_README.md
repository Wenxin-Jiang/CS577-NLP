---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-10front-1body-10rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-10front-1body-10rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4366
- Wer: 0.1693
- Mer: 0.1636
- Wil: 0.2493
- Wip: 0.7507
- Hits: 55904
- Substitutions: 6304
- Deletions: 2379
- Insertions: 2249
- Cer: 0.1332

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
- seed: 40
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    | Mer    | Wil    | Wip    | Hits  | Substitutions | Deletions | Insertions | Cer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:------:|:------:|:-----:|:-------------:|:---------:|:----------:|:------:|
| 0.6166        | 1.0   | 1457  | 0.4595          | 0.2096 | 0.1979 | 0.2878 | 0.7122 | 54866 | 6757          | 2964      | 3819       | 0.1793 |
| 0.4985        | 2.0   | 2914  | 0.4190          | 0.1769 | 0.1710 | 0.2587 | 0.7413 | 55401 | 6467          | 2719      | 2241       | 0.1417 |
| 0.4787        | 3.0   | 4371  | 0.4130          | 0.1728 | 0.1670 | 0.2534 | 0.7466 | 55677 | 6357          | 2553      | 2249       | 0.1368 |
| 0.4299        | 4.0   | 5828  | 0.4085          | 0.1726 | 0.1665 | 0.2530 | 0.7470 | 55799 | 6381          | 2407      | 2357       | 0.1348 |
| 0.3855        | 5.0   | 7285  | 0.4130          | 0.1702 | 0.1644 | 0.2501 | 0.7499 | 55887 | 6309          | 2391      | 2292       | 0.1336 |
| 0.3109        | 6.0   | 8742  | 0.4182          | 0.1732 | 0.1668 | 0.2525 | 0.7475 | 55893 | 6317          | 2377      | 2494       | 0.1450 |
| 0.3027        | 7.0   | 10199 | 0.4256          | 0.1691 | 0.1633 | 0.2486 | 0.7514 | 55949 | 6273          | 2365      | 2283       | 0.1325 |
| 0.2729        | 8.0   | 11656 | 0.4252          | 0.1709 | 0.1649 | 0.2503 | 0.7497 | 55909 | 6283          | 2395      | 2362       | 0.1375 |
| 0.2531        | 9.0   | 13113 | 0.4329          | 0.1696 | 0.1639 | 0.2499 | 0.7501 | 55870 | 6322          | 2395      | 2235       | 0.1334 |
| 0.2388        | 10.0  | 14570 | 0.4366          | 0.1693 | 0.1636 | 0.2493 | 0.7507 | 55904 | 6304          | 2379      | 2249       | 0.1332 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
