---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-0front-1body-9rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-0front-1body-9rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4673
- Wer: 0.1766
- Mer: 0.1707
- Wil: 0.2594
- Wip: 0.7406
- Hits: 55410
- Substitutions: 6552
- Deletions: 2625
- Insertions: 2229
- Cer: 0.1386

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
| 0.641         | 1.0   | 1457  | 0.4913          | 0.2084 | 0.1972 | 0.2875 | 0.7125 | 54788 | 6785          | 3014      | 3658       | 0.1743 |
| 0.5415        | 2.0   | 2914  | 0.4483          | 0.1818 | 0.1759 | 0.2643 | 0.7357 | 55033 | 6514          | 3040      | 2190       | 0.1447 |
| 0.4835        | 3.0   | 4371  | 0.4427          | 0.1785 | 0.1722 | 0.2595 | 0.7405 | 55442 | 6443          | 2702      | 2386       | 0.1402 |
| 0.4267        | 4.0   | 5828  | 0.4376          | 0.1769 | 0.1711 | 0.2587 | 0.7413 | 55339 | 6446          | 2802      | 2177       | 0.1399 |
| 0.3752        | 5.0   | 7285  | 0.4414          | 0.1756 | 0.1698 | 0.2571 | 0.7429 | 55467 | 6432          | 2688      | 2223       | 0.1374 |
| 0.3471        | 6.0   | 8742  | 0.4497          | 0.1761 | 0.1704 | 0.2585 | 0.7415 | 55379 | 6494          | 2714      | 2166       | 0.1380 |
| 0.3841        | 7.0   | 10199 | 0.4535          | 0.1769 | 0.1710 | 0.2589 | 0.7411 | 55383 | 6482          | 2722      | 2220       | 0.1394 |
| 0.3139        | 8.0   | 11656 | 0.4604          | 0.1753 | 0.1696 | 0.2577 | 0.7423 | 55462 | 6502          | 2623      | 2199       | 0.1367 |
| 0.3012        | 9.0   | 13113 | 0.4628          | 0.1766 | 0.1708 | 0.2597 | 0.7403 | 55391 | 6571          | 2625      | 2210       | 0.1388 |
| 0.3087        | 10.0  | 14570 | 0.4673          | 0.1766 | 0.1707 | 0.2594 | 0.7406 | 55410 | 6552          | 2625      | 2229       | 0.1386 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
