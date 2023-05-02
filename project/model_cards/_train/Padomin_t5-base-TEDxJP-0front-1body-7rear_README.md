---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-0front-1body-7rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-0front-1body-7rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4666
- Wer: 0.1780
- Mer: 0.1718
- Wil: 0.2607
- Wip: 0.7393
- Hits: 55410
- Substitutions: 6566
- Deletions: 2611
- Insertions: 2321
- Cer: 0.1388

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
| 0.6424        | 1.0   | 1457  | 0.4944          | 0.1980 | 0.1893 | 0.2798 | 0.7202 | 54775 | 6748          | 3064      | 2975       | 0.1603 |
| 0.5444        | 2.0   | 2914  | 0.4496          | 0.1799 | 0.1740 | 0.2619 | 0.7381 | 55175 | 6480          | 2932      | 2207       | 0.1400 |
| 0.4975        | 3.0   | 4371  | 0.4451          | 0.1773 | 0.1713 | 0.2586 | 0.7414 | 55399 | 6429          | 2759      | 2266       | 0.1397 |
| 0.4312        | 4.0   | 5828  | 0.4417          | 0.1758 | 0.1701 | 0.2572 | 0.7428 | 55408 | 6407          | 2772      | 2178       | 0.1378 |
| 0.3846        | 5.0   | 7285  | 0.4445          | 0.1753 | 0.1696 | 0.2573 | 0.7427 | 55409 | 6453          | 2725      | 2142       | 0.1367 |
| 0.3501        | 6.0   | 8742  | 0.4482          | 0.1792 | 0.1727 | 0.2609 | 0.7391 | 55453 | 6522          | 2612      | 2439       | 0.1401 |
| 0.381         | 7.0   | 10199 | 0.4531          | 0.1770 | 0.1711 | 0.2592 | 0.7408 | 55380 | 6498          | 2709      | 2223       | 0.1378 |
| 0.313         | 8.0   | 11656 | 0.4585          | 0.1775 | 0.1716 | 0.2599 | 0.7401 | 55371 | 6516          | 2700      | 2250       | 0.1383 |
| 0.2976        | 9.0   | 13113 | 0.4646          | 0.1778 | 0.1717 | 0.2603 | 0.7397 | 55387 | 6537          | 2663      | 2284       | 0.1402 |
| 0.3152        | 10.0  | 14570 | 0.4666          | 0.1780 | 0.1718 | 0.2607 | 0.7393 | 55410 | 6566          | 2611      | 2321       | 0.1388 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
