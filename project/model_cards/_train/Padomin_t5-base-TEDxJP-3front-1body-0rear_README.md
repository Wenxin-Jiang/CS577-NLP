---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-3front-1body-0rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-3front-1body-0rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4641
- Wer: 0.1743
- Mer: 0.1684
- Wil: 0.2557
- Wip: 0.7443
- Hits: 55594
- Substitutions: 6428
- Deletions: 2565
- Insertions: 2267
- Cer: 0.1368

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
| 0.6567        | 1.0   | 1457  | 0.4959          | 0.2072 | 0.1966 | 0.2877 | 0.7123 | 54688 | 6836          | 3063      | 3486       | 0.1936 |
| 0.5486        | 2.0   | 2914  | 0.4504          | 0.1870 | 0.1796 | 0.2677 | 0.7323 | 55158 | 6518          | 2911      | 2647       | 0.1528 |
| 0.4957        | 3.0   | 4371  | 0.4410          | 0.1764 | 0.1705 | 0.2578 | 0.7422 | 55412 | 6429          | 2746      | 2216       | 0.1375 |
| 0.4371        | 4.0   | 5828  | 0.4379          | 0.1761 | 0.1702 | 0.2572 | 0.7428 | 55447 | 6407          | 2733      | 2232       | 0.1377 |
| 0.387         | 5.0   | 7285  | 0.4408          | 0.1756 | 0.1696 | 0.2562 | 0.7438 | 55510 | 6372          | 2705      | 2263       | 0.1399 |
| 0.3589        | 6.0   | 8742  | 0.4466          | 0.1737 | 0.1681 | 0.2552 | 0.7448 | 55532 | 6406          | 2649      | 2165       | 0.1359 |
| 0.3876        | 7.0   | 10199 | 0.4532          | 0.1746 | 0.1689 | 0.2563 | 0.7437 | 55491 | 6436          | 2660      | 2179       | 0.1363 |
| 0.3199        | 8.0   | 11656 | 0.4591          | 0.1738 | 0.1681 | 0.2554 | 0.7446 | 55568 | 6431          | 2588      | 2208       | 0.1362 |
| 0.3079        | 9.0   | 13113 | 0.4625          | 0.1743 | 0.1685 | 0.2557 | 0.7443 | 55579 | 6425          | 2583      | 2252       | 0.1366 |
| 0.3124        | 10.0  | 14570 | 0.4641          | 0.1743 | 0.1684 | 0.2557 | 0.7443 | 55594 | 6428          | 2565      | 2267       | 0.1368 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
