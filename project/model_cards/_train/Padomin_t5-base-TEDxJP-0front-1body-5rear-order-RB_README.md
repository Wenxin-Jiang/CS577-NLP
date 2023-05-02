---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-0front-1body-5rear-order-RB
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-0front-1body-5rear-order-RB

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4744
- Wer: 0.1790
- Mer: 0.1727
- Wil: 0.2610
- Wip: 0.7390
- Hits: 55379
- Substitutions: 6518
- Deletions: 2690
- Insertions: 2353
- Cer: 0.1409

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
- seed: 40
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    | Mer    | Wil    | Wip    | Hits  | Substitutions | Deletions | Insertions | Cer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:------:|:------:|:-----:|:-------------:|:---------:|:----------:|:------:|
| 0.6463        | 1.0   | 1457  | 0.4971          | 0.2539 | 0.2313 | 0.3198 | 0.6802 | 54480 | 6786          | 3321      | 6290       | 0.2360 |
| 0.5488        | 2.0   | 2914  | 0.4629          | 0.1840 | 0.1776 | 0.2664 | 0.7336 | 55044 | 6557          | 2986      | 2342       | 0.1488 |
| 0.553         | 3.0   | 4371  | 0.4522          | 0.1792 | 0.1734 | 0.2615 | 0.7385 | 55160 | 6487          | 2940      | 2145       | 0.1421 |
| 0.4962        | 4.0   | 5828  | 0.4488          | 0.1801 | 0.1737 | 0.2615 | 0.7385 | 55350 | 6484          | 2753      | 2395       | 0.1424 |
| 0.4629        | 5.0   | 7285  | 0.4534          | 0.1794 | 0.1732 | 0.2617 | 0.7383 | 55330 | 6540          | 2717      | 2330       | 0.1407 |
| 0.3637        | 6.0   | 8742  | 0.4577          | 0.1797 | 0.1732 | 0.2614 | 0.7386 | 55402 | 6516          | 2669      | 2421       | 0.1412 |
| 0.3499        | 7.0   | 10199 | 0.4645          | 0.1780 | 0.1719 | 0.2598 | 0.7402 | 55411 | 6486          | 2690      | 2323       | 0.1393 |
| 0.3261        | 8.0   | 11656 | 0.4660          | 0.1785 | 0.1722 | 0.2604 | 0.7396 | 55416 | 6512          | 2659      | 2358       | 0.1400 |
| 0.3089        | 9.0   | 13113 | 0.4719          | 0.1790 | 0.1727 | 0.2613 | 0.7387 | 55371 | 6549          | 2667      | 2342       | 0.1407 |
| 0.3024        | 10.0  | 14570 | 0.4744          | 0.1790 | 0.1727 | 0.2610 | 0.7390 | 55379 | 6518          | 2690      | 2353       | 0.1409 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
