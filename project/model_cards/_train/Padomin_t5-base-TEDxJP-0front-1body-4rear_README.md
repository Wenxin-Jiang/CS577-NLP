---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-0front-1body-4rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-0front-1body-4rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4720
- Wer: 0.1769
- Mer: 0.1709
- Wil: 0.2591
- Wip: 0.7409
- Hits: 55442
- Substitutions: 6513
- Deletions: 2632
- Insertions: 2280
- Cer: 0.1387

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
| 0.6395        | 1.0   | 1457  | 0.4943          | 0.2206 | 0.2065 | 0.2967 | 0.7033 | 54738 | 6822          | 3027      | 4400       | 0.1942 |
| 0.5522        | 2.0   | 2914  | 0.4580          | 0.1811 | 0.1752 | 0.2633 | 0.7367 | 55065 | 6491          | 3031      | 2172       | 0.1522 |
| 0.4967        | 3.0   | 4371  | 0.4486          | 0.1794 | 0.1733 | 0.2614 | 0.7386 | 55295 | 6502          | 2790      | 2296       | 0.1424 |
| 0.4355        | 4.0   | 5828  | 0.4471          | 0.1776 | 0.1717 | 0.2598 | 0.7402 | 55331 | 6493          | 2763      | 2215       | 0.1410 |
| 0.3915        | 5.0   | 7285  | 0.4478          | 0.1770 | 0.1712 | 0.2593 | 0.7407 | 55352 | 6493          | 2742      | 2196       | 0.1398 |
| 0.3686        | 6.0   | 8742  | 0.4542          | 0.1785 | 0.1722 | 0.2610 | 0.7390 | 55416 | 6562          | 2609      | 2358       | 0.1423 |
| 0.3957        | 7.0   | 10199 | 0.4577          | 0.1779 | 0.1719 | 0.2603 | 0.7397 | 55349 | 6523          | 2715      | 2250       | 0.1446 |
| 0.3235        | 8.0   | 11656 | 0.4634          | 0.1760 | 0.1703 | 0.2587 | 0.7413 | 55380 | 6514          | 2693      | 2163       | 0.1390 |
| 0.3175        | 9.0   | 13113 | 0.4696          | 0.1772 | 0.1712 | 0.2598 | 0.7402 | 55407 | 6539          | 2641      | 2266       | 0.1388 |
| 0.3213        | 10.0  | 14570 | 0.4720          | 0.1769 | 0.1709 | 0.2591 | 0.7409 | 55442 | 6513          | 2632      | 2280       | 0.1387 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
