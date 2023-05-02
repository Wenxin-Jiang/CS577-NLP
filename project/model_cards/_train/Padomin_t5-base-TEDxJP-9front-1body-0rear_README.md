---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-9front-1body-0rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-9front-1body-0rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4576
- Wer: 0.1728
- Mer: 0.1669
- Wil: 0.2543
- Wip: 0.7457
- Hits: 55705
- Substitutions: 6444
- Deletions: 2438
- Insertions: 2281
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
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    | Mer    | Wil    | Wip    | Hits  | Substitutions | Deletions | Insertions | Cer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:------:|:------:|:-----:|:-------------:|:---------:|:----------:|:------:|
| 0.649         | 1.0   | 1457  | 0.4844          | 0.2290 | 0.2126 | 0.3015 | 0.6985 | 54758 | 6748          | 3081      | 4959       | 0.2080 |
| 0.5319        | 2.0   | 2914  | 0.4385          | 0.1804 | 0.1741 | 0.2614 | 0.7386 | 55298 | 6437          | 2852      | 2364       | 0.1465 |
| 0.4819        | 3.0   | 4371  | 0.4338          | 0.1760 | 0.1698 | 0.2569 | 0.7431 | 55558 | 6419          | 2610      | 2336       | 0.1389 |
| 0.4307        | 4.0   | 5828  | 0.4328          | 0.1759 | 0.1696 | 0.2569 | 0.7431 | 55649 | 6454          | 2484      | 2424       | 0.1390 |
| 0.3735        | 5.0   | 7285  | 0.4331          | 0.1740 | 0.1680 | 0.2549 | 0.7451 | 55652 | 6398          | 2537      | 2306       | 0.1367 |
| 0.3495        | 6.0   | 8742  | 0.4380          | 0.1740 | 0.1681 | 0.2552 | 0.7448 | 55619 | 6420          | 2548      | 2267       | 0.1356 |
| 0.3679        | 7.0   | 10199 | 0.4437          | 0.1741 | 0.1682 | 0.2556 | 0.7444 | 55621 | 6441          | 2525      | 2281       | 0.1354 |
| 0.3035        | 8.0   | 11656 | 0.4494          | 0.1727 | 0.1669 | 0.2542 | 0.7458 | 55672 | 6433          | 2482      | 2237       | 0.1350 |
| 0.3041        | 9.0   | 13113 | 0.4541          | 0.1736 | 0.1677 | 0.2550 | 0.7450 | 55674 | 6441          | 2472      | 2302       | 0.1383 |
| 0.2948        | 10.0  | 14570 | 0.4576          | 0.1728 | 0.1669 | 0.2543 | 0.7457 | 55705 | 6444          | 2438      | 2281       | 0.1351 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
