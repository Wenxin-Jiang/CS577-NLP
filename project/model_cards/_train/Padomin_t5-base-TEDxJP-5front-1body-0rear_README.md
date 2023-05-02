---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-5front-1body-0rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-5front-1body-0rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4633
- Wer: 0.1756
- Mer: 0.1693
- Wil: 0.2562
- Wip: 0.7438
- Hits: 55657
- Substitutions: 6415
- Deletions: 2515
- Insertions: 2414
- Cer: 0.1382

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
| 0.6441        | 1.0   | 1457  | 0.4872          | 0.2061 | 0.1954 | 0.2850 | 0.7150 | 54813 | 6709          | 3065      | 3540       | 0.1823 |
| 0.543         | 2.0   | 2914  | 0.4422          | 0.1832 | 0.1765 | 0.2641 | 0.7359 | 55188 | 6458          | 2941      | 2432       | 0.1491 |
| 0.4896        | 3.0   | 4371  | 0.4373          | 0.1811 | 0.1739 | 0.2612 | 0.7388 | 55568 | 6464          | 2555      | 2679       | 0.1450 |
| 0.4299        | 4.0   | 5828  | 0.4326          | 0.1745 | 0.1685 | 0.2553 | 0.7447 | 55604 | 6391          | 2592      | 2288       | 0.1367 |
| 0.3853        | 5.0   | 7285  | 0.4390          | 0.1758 | 0.1693 | 0.2561 | 0.7439 | 55696 | 6406          | 2485      | 2462       | 0.1375 |
| 0.357         | 6.0   | 8742  | 0.4433          | 0.1835 | 0.1757 | 0.2619 | 0.7381 | 55609 | 6386          | 2592      | 2871       | 0.1438 |
| 0.3735        | 7.0   | 10199 | 0.4479          | 0.1799 | 0.1729 | 0.2598 | 0.7402 | 55582 | 6425          | 2580      | 2617       | 0.1411 |
| 0.302         | 8.0   | 11656 | 0.4554          | 0.1770 | 0.1702 | 0.2569 | 0.7431 | 55725 | 6408          | 2454      | 2568       | 0.1386 |
| 0.2992        | 9.0   | 13113 | 0.4614          | 0.1784 | 0.1715 | 0.2581 | 0.7419 | 55672 | 6405          | 2510      | 2606       | 0.1404 |
| 0.2972        | 10.0  | 14570 | 0.4633          | 0.1756 | 0.1693 | 0.2562 | 0.7438 | 55657 | 6415          | 2515      | 2414       | 0.1382 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
