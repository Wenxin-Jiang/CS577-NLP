---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-7front-1body-0rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-7front-1body-0rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4563
- Wer: 0.1763
- Mer: 0.1699
- Wil: 0.2573
- Wip: 0.7427
- Hits: 55638
- Substitutions: 6453
- Deletions: 2496
- Insertions: 2439
- Cer: 0.1383

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
| 0.6569        | 1.0   | 1457  | 0.4908          | 0.2308 | 0.2137 | 0.3042 | 0.6958 | 54844 | 6924          | 2819      | 5165       | 0.2114 |
| 0.5393        | 2.0   | 2914  | 0.4417          | 0.1916 | 0.1830 | 0.2706 | 0.7294 | 55263 | 6515          | 2809      | 3053       | 0.1559 |
| 0.4959        | 3.0   | 4371  | 0.4334          | 0.1776 | 0.1709 | 0.2574 | 0.7426 | 55660 | 6391          | 2536      | 2543       | 0.1398 |
| 0.4306        | 4.0   | 5828  | 0.4302          | 0.1755 | 0.1693 | 0.2563 | 0.7437 | 55618 | 6414          | 2555      | 2367       | 0.1372 |
| 0.3862        | 5.0   | 7285  | 0.4321          | 0.1752 | 0.1690 | 0.2561 | 0.7439 | 55653 | 6430          | 2504      | 2384       | 0.1369 |
| 0.3423        | 6.0   | 8742  | 0.4376          | 0.1772 | 0.1705 | 0.2576 | 0.7424 | 55660 | 6430          | 2497      | 2517       | 0.1384 |
| 0.3705        | 7.0   | 10199 | 0.4438          | 0.1746 | 0.1686 | 0.2559 | 0.7441 | 55589 | 6431          | 2567      | 2277       | 0.1358 |
| 0.2991        | 8.0   | 11656 | 0.4484          | 0.1763 | 0.1698 | 0.2571 | 0.7429 | 55650 | 6444          | 2493      | 2448       | 0.1382 |
| 0.2903        | 9.0   | 13113 | 0.4541          | 0.1764 | 0.1699 | 0.2570 | 0.7430 | 55655 | 6428          | 2504      | 2461       | 0.1384 |
| 0.2937        | 10.0  | 14570 | 0.4563          | 0.1763 | 0.1699 | 0.2573 | 0.7427 | 55638 | 6453          | 2496      | 2439       | 0.1383 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
