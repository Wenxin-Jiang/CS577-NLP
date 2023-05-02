---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-0front-1body-1rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-0front-1body-1rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4869
- Wer: 0.1801
- Mer: 0.1739
- Wil: 0.2635
- Wip: 0.7365
- Hits: 55253
- Substitutions: 6626
- Deletions: 2708
- Insertions: 2296
- Cer: 0.1411

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
| 0.6609        | 1.0   | 1457  | 0.5121          | 0.2181 | 0.2049 | 0.2958 | 0.7042 | 54651 | 6867          | 3069      | 4151       | 0.1880 |
| 0.5633        | 2.0   | 2914  | 0.4719          | 0.1891 | 0.1817 | 0.2714 | 0.7286 | 55015 | 6654          | 2918      | 2644       | 0.1558 |
| 0.5212        | 3.0   | 4371  | 0.4626          | 0.1838 | 0.1771 | 0.2666 | 0.7334 | 55168 | 6635          | 2784      | 2452       | 0.1462 |
| 0.4498        | 4.0   | 5828  | 0.4616          | 0.1807 | 0.1747 | 0.2643 | 0.7357 | 55148 | 6630          | 2809      | 2231       | 0.1420 |
| 0.4058        | 5.0   | 7285  | 0.4633          | 0.1799 | 0.1739 | 0.2631 | 0.7369 | 55200 | 6592          | 2795      | 2231       | 0.1419 |
| 0.3802        | 6.0   | 8742  | 0.4675          | 0.1796 | 0.1733 | 0.2630 | 0.7370 | 55311 | 6636          | 2640      | 2321       | 0.1412 |
| 0.4126        | 7.0   | 10199 | 0.4737          | 0.1781 | 0.1724 | 0.2617 | 0.7383 | 55245 | 6595          | 2747      | 2163       | 0.1394 |
| 0.3436        | 8.0   | 11656 | 0.4772          | 0.1788 | 0.1729 | 0.2624 | 0.7376 | 55247 | 6616          | 2724      | 2208       | 0.1401 |
| 0.3249        | 9.0   | 13113 | 0.4827          | 0.1796 | 0.1735 | 0.2632 | 0.7368 | 55265 | 6635          | 2687      | 2281       | 0.1407 |
| 0.3347        | 10.0  | 14570 | 0.4869          | 0.1801 | 0.1739 | 0.2635 | 0.7365 | 55253 | 6626          | 2708      | 2296       | 0.1411 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
