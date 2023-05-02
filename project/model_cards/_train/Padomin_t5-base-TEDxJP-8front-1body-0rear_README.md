---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-8front-1body-0rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-8front-1body-0rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4589
- Wer: 0.1739
- Mer: 0.1679
- Wil: 0.2545
- Wip: 0.7455
- Hits: 55667
- Substitutions: 6385
- Deletions: 2535
- Insertions: 2309
- Cer: 0.1363

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
| 0.6586        | 1.0   | 1457  | 0.4812          | 0.2110 | 0.1994 | 0.2888 | 0.7112 | 54745 | 6712          | 3130      | 3789       | 0.1784 |
| 0.5246        | 2.0   | 2914  | 0.4383          | 0.1839 | 0.1770 | 0.2641 | 0.7359 | 55251 | 6428          | 2908      | 2544       | 0.1481 |
| 0.4795        | 3.0   | 4371  | 0.4327          | 0.1811 | 0.1740 | 0.2610 | 0.7390 | 55523 | 6438          | 2626      | 2631       | 0.1458 |
| 0.4224        | 4.0   | 5828  | 0.4328          | 0.1754 | 0.1693 | 0.2555 | 0.7445 | 55577 | 6338          | 2672      | 2318       | 0.1397 |
| 0.3755        | 5.0   | 7285  | 0.4351          | 0.1723 | 0.1668 | 0.2529 | 0.7471 | 55607 | 6326          | 2654      | 2150       | 0.1362 |
| 0.3538        | 6.0   | 8742  | 0.4413          | 0.1728 | 0.1670 | 0.2531 | 0.7469 | 55696 | 6341          | 2550      | 2271       | 0.1372 |
| 0.3686        | 7.0   | 10199 | 0.4455          | 0.1715 | 0.1659 | 0.2519 | 0.7481 | 55692 | 6319          | 2576      | 2180       | 0.1354 |
| 0.3004        | 8.0   | 11656 | 0.4518          | 0.1727 | 0.1668 | 0.2537 | 0.7463 | 55712 | 6400          | 2475      | 2281       | 0.1371 |
| 0.2914        | 9.0   | 13113 | 0.4564          | 0.1739 | 0.1678 | 0.2544 | 0.7456 | 55681 | 6378          | 2528      | 2323       | 0.1370 |
| 0.297         | 10.0  | 14570 | 0.4589          | 0.1739 | 0.1679 | 0.2545 | 0.7455 | 55667 | 6385          | 2535      | 2309       | 0.1363 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
