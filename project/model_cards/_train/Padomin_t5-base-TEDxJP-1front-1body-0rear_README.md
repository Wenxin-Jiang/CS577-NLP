---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-1front-1body-0rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-1front-1body-0rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4787
- Wer: 0.1786
- Mer: 0.1722
- Wil: 0.2608
- Wip: 0.7392
- Hits: 55434
- Substitutions: 6554
- Deletions: 2599
- Insertions: 2380
- Cer: 0.1399

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
| 0.6606        | 1.0   | 1457  | 0.5113          | 0.2142 | 0.2017 | 0.2939 | 0.7061 | 54751 | 6976          | 2860      | 4000       | 0.1909 |
| 0.5636        | 2.0   | 2914  | 0.4669          | 0.1913 | 0.1832 | 0.2728 | 0.7272 | 55086 | 6669          | 2832      | 2852       | 0.1700 |
| 0.5115        | 3.0   | 4371  | 0.4543          | 0.1815 | 0.1747 | 0.2633 | 0.7367 | 55384 | 6559          | 2644      | 2519       | 0.1504 |
| 0.4463        | 4.0   | 5828  | 0.4512          | 0.1796 | 0.1733 | 0.2617 | 0.7383 | 55344 | 6534          | 2709      | 2358       | 0.1422 |
| 0.4001        | 5.0   | 7285  | 0.4564          | 0.1779 | 0.1718 | 0.2600 | 0.7400 | 55394 | 6509          | 2684      | 2295       | 0.1395 |
| 0.3683        | 6.0   | 8742  | 0.4600          | 0.1790 | 0.1726 | 0.2611 | 0.7389 | 55436 | 6546          | 2605      | 2413       | 0.1405 |
| 0.391         | 7.0   | 10199 | 0.4651          | 0.1781 | 0.1718 | 0.2599 | 0.7401 | 55424 | 6505          | 2658      | 2338       | 0.1391 |
| 0.337         | 8.0   | 11656 | 0.4705          | 0.1775 | 0.1714 | 0.2595 | 0.7405 | 55439 | 6511          | 2637      | 2316       | 0.1382 |
| 0.3233        | 9.0   | 13113 | 0.4757          | 0.1790 | 0.1726 | 0.2612 | 0.7388 | 55414 | 6554          | 2619      | 2386       | 0.1401 |
| 0.3204        | 10.0  | 14570 | 0.4787          | 0.1786 | 0.1722 | 0.2608 | 0.7392 | 55434 | 6554          | 2599      | 2380       | 0.1399 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
