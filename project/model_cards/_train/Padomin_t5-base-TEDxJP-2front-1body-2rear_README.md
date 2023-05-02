---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-2front-1body-2rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-2front-1body-2rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4506
- Wer: 0.1731
- Mer: 0.1672
- Wil: 0.2543
- Wip: 0.7457
- Hits: 55684
- Substitutions: 6416
- Deletions: 2487
- Insertions: 2280
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
| 0.6398        | 1.0   | 1457  | 0.4851          | 0.2123 | 0.1997 | 0.2912 | 0.7088 | 54936 | 6930          | 2721      | 4058       | 0.1854 |
| 0.525         | 2.0   | 2914  | 0.4364          | 0.1800 | 0.1735 | 0.2623 | 0.7377 | 55355 | 6566          | 2666      | 2392       | 0.1406 |
| 0.4731        | 3.0   | 4371  | 0.4294          | 0.1796 | 0.1728 | 0.2600 | 0.7400 | 55542 | 6444          | 2601      | 2558       | 0.1417 |
| 0.4093        | 4.0   | 5828  | 0.4291          | 0.1728 | 0.1670 | 0.2541 | 0.7459 | 55667 | 6419          | 2501      | 2238       | 0.1349 |
| 0.3718        | 5.0   | 7285  | 0.4285          | 0.1727 | 0.1669 | 0.2542 | 0.7458 | 55657 | 6430          | 2500      | 2223       | 0.1351 |
| 0.3436        | 6.0   | 8742  | 0.4318          | 0.1725 | 0.1669 | 0.2541 | 0.7459 | 55614 | 6412          | 2561      | 2171       | 0.1361 |
| 0.371         | 7.0   | 10199 | 0.4382          | 0.1722 | 0.1665 | 0.2530 | 0.7470 | 55664 | 6361          | 2562      | 2197       | 0.1351 |
| 0.3007        | 8.0   | 11656 | 0.4427          | 0.1726 | 0.1668 | 0.2535 | 0.7465 | 55691 | 6380          | 2516      | 2252       | 0.1357 |
| 0.2997        | 9.0   | 13113 | 0.4464          | 0.1731 | 0.1672 | 0.2543 | 0.7457 | 55682 | 6420          | 2485      | 2276       | 0.1362 |
| 0.2969        | 10.0  | 14570 | 0.4506          | 0.1731 | 0.1672 | 0.2543 | 0.7457 | 55684 | 6416          | 2487      | 2280       | 0.1363 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
