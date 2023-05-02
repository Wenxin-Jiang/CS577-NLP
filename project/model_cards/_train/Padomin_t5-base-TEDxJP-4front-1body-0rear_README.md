---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-4front-1body-0rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-4front-1body-0rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4643
- Wer: 0.1751
- Mer: 0.1690
- Wil: 0.2562
- Wip: 0.7438
- Hits: 55598
- Substitutions: 6434
- Deletions: 2555
- Insertions: 2317
- Cer: 0.1374

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
| 0.6492        | 1.0   | 1457  | 0.4952          | 0.2272 | 0.2114 | 0.3015 | 0.6985 | 54739 | 6847          | 3001      | 4827       | 0.2013 |
| 0.5556        | 2.0   | 2914  | 0.4456          | 0.1899 | 0.1818 | 0.2686 | 0.7314 | 55189 | 6420          | 2978      | 2864       | 0.1558 |
| 0.4942        | 3.0   | 4371  | 0.4423          | 0.1814 | 0.1743 | 0.2614 | 0.7386 | 55493 | 6437          | 2657      | 2623       | 0.1457 |
| 0.4326        | 4.0   | 5828  | 0.4361          | 0.1749 | 0.1690 | 0.2561 | 0.7439 | 55542 | 6419          | 2626      | 2249       | 0.1362 |
| 0.3867        | 5.0   | 7285  | 0.4395          | 0.1752 | 0.1692 | 0.2559 | 0.7441 | 55542 | 6378          | 2667      | 2270       | 0.1374 |
| 0.3501        | 6.0   | 8742  | 0.4487          | 0.1751 | 0.1691 | 0.2565 | 0.7435 | 55598 | 6448          | 2541      | 2323       | 0.1366 |
| 0.3835        | 7.0   | 10199 | 0.4494          | 0.1744 | 0.1685 | 0.2556 | 0.7444 | 55594 | 6416          | 2577      | 2274       | 0.1378 |
| 0.3013        | 8.0   | 11656 | 0.4580          | 0.1744 | 0.1685 | 0.2563 | 0.7437 | 55570 | 6467          | 2550      | 2248       | 0.1366 |
| 0.3126        | 9.0   | 13113 | 0.4598          | 0.1749 | 0.1689 | 0.2564 | 0.7436 | 55571 | 6447          | 2569      | 2281       | 0.1376 |
| 0.3089        | 10.0  | 14570 | 0.4643          | 0.1751 | 0.1690 | 0.2562 | 0.7438 | 55598 | 6434          | 2555      | 2317       | 0.1374 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
