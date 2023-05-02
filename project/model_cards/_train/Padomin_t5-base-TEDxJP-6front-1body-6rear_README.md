---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-6front-1body-6rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-6front-1body-6rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4394
- Wer: 0.1704
- Mer: 0.1647
- Wil: 0.2508
- Wip: 0.7492
- Hits: 55836
- Substitutions: 6340
- Deletions: 2411
- Insertions: 2256
- Cer: 0.1351

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
| 0.6164        | 1.0   | 1457  | 0.4627          | 0.2224 | 0.2073 | 0.2961 | 0.7039 | 54939 | 6736          | 2912      | 4716       | 0.1954 |
| 0.5064        | 2.0   | 2914  | 0.4222          | 0.1785 | 0.1722 | 0.2591 | 0.7409 | 55427 | 6402          | 2758      | 2370       | 0.1416 |
| 0.4909        | 3.0   | 4371  | 0.4147          | 0.1717 | 0.1664 | 0.2514 | 0.7486 | 55563 | 6218          | 2806      | 2068       | 0.1350 |
| 0.4365        | 4.0   | 5828  | 0.4120          | 0.1722 | 0.1661 | 0.2525 | 0.7475 | 55848 | 6373          | 2366      | 2385       | 0.1380 |
| 0.3954        | 5.0   | 7285  | 0.4145          | 0.1715 | 0.1655 | 0.2517 | 0.7483 | 55861 | 6355          | 2371      | 2351       | 0.1384 |
| 0.3181        | 6.0   | 8742  | 0.4178          | 0.1710 | 0.1650 | 0.2509 | 0.7491 | 55891 | 6326          | 2370      | 2348       | 0.1368 |
| 0.2971        | 7.0   | 10199 | 0.4261          | 0.1698 | 0.1640 | 0.2497 | 0.7503 | 55900 | 6304          | 2383      | 2279       | 0.1348 |
| 0.2754        | 8.0   | 11656 | 0.4299          | 0.1703 | 0.1645 | 0.2504 | 0.7496 | 55875 | 6320          | 2392      | 2288       | 0.1354 |
| 0.2604        | 9.0   | 13113 | 0.4371          | 0.1702 | 0.1644 | 0.2506 | 0.7494 | 55864 | 6343          | 2380      | 2267       | 0.1347 |
| 0.2477        | 10.0  | 14570 | 0.4394          | 0.1704 | 0.1647 | 0.2508 | 0.7492 | 55836 | 6340          | 2411      | 2256       | 0.1351 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
