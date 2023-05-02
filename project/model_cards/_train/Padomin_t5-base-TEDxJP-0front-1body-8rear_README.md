---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-0front-1body-8rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-0front-1body-8rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4672
- Wer: 0.1759
- Mer: 0.1698
- Wil: 0.2574
- Wip: 0.7426
- Hits: 55537
- Substitutions: 6457
- Deletions: 2593
- Insertions: 2312
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
| 0.6417        | 1.0   | 1457  | 0.4928          | 0.2086 | 0.1973 | 0.2873 | 0.7127 | 54805 | 6751          | 3031      | 3693       | 0.1746 |
| 0.5435        | 2.0   | 2914  | 0.4511          | 0.1814 | 0.1751 | 0.2634 | 0.7366 | 55192 | 6518          | 2877      | 2322       | 0.1452 |
| 0.4914        | 3.0   | 4371  | 0.4424          | 0.1762 | 0.1704 | 0.2572 | 0.7428 | 55389 | 6383          | 2815      | 2180       | 0.1390 |
| 0.427         | 4.0   | 5828  | 0.4388          | 0.1751 | 0.1695 | 0.2569 | 0.7431 | 55408 | 6431          | 2748      | 2129       | 0.1366 |
| 0.3762        | 5.0   | 7285  | 0.4465          | 0.1747 | 0.1689 | 0.2561 | 0.7439 | 55533 | 6424          | 2630      | 2230       | 0.1361 |
| 0.3562        | 6.0   | 8742  | 0.4505          | 0.1761 | 0.1700 | 0.2581 | 0.7419 | 55558 | 6507          | 2522      | 2348       | 0.1402 |
| 0.3884        | 7.0   | 10199 | 0.4550          | 0.1750 | 0.1691 | 0.2564 | 0.7436 | 55548 | 6439          | 2600      | 2264       | 0.1364 |
| 0.3144        | 8.0   | 11656 | 0.4616          | 0.1760 | 0.1698 | 0.2572 | 0.7428 | 55571 | 6447          | 2569      | 2352       | 0.1373 |
| 0.3075        | 9.0   | 13113 | 0.4660          | 0.1761 | 0.1700 | 0.2572 | 0.7428 | 55547 | 6431          | 2609      | 2336       | 0.1400 |
| 0.3152        | 10.0  | 14570 | 0.4672          | 0.1759 | 0.1698 | 0.2574 | 0.7426 | 55537 | 6457          | 2593      | 2312       | 0.1383 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
