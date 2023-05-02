---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-10front-1body-0rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-10front-1body-0rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4586
- Wer: 0.1729
- Mer: 0.1671
- Wil: 0.2545
- Wip: 0.7455
- Hits: 55669
- Substitutions: 6448
- Deletions: 2470
- Insertions: 2249
- Cer: 0.1350

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
| 0.6477        | 1.0   | 1457  | 0.4829          | 0.2234 | 0.2082 | 0.2973 | 0.7027 | 54891 | 6766          | 2930      | 4734       | 0.2060 |
| 0.5306        | 2.0   | 2914  | 0.4366          | 0.1808 | 0.1743 | 0.2615 | 0.7385 | 55312 | 6431          | 2844      | 2402       | 0.1439 |
| 0.4743        | 3.0   | 4371  | 0.4311          | 0.1827 | 0.1752 | 0.2623 | 0.7377 | 55558 | 6456          | 2573      | 2771       | 0.1483 |
| 0.4299        | 4.0   | 5828  | 0.4286          | 0.1778 | 0.1711 | 0.2580 | 0.7420 | 55641 | 6422          | 2524      | 2540       | 0.1419 |
| 0.3815        | 5.0   | 7285  | 0.4321          | 0.1741 | 0.1680 | 0.2554 | 0.7446 | 55673 | 6448          | 2466      | 2330       | 0.1379 |
| 0.3508        | 6.0   | 8742  | 0.4392          | 0.1737 | 0.1677 | 0.2547 | 0.7453 | 55683 | 6417          | 2487      | 2312       | 0.1373 |
| 0.3594        | 7.0   | 10199 | 0.4477          | 0.1726 | 0.1666 | 0.2528 | 0.7472 | 55757 | 6344          | 2486      | 2319       | 0.1349 |
| 0.2975        | 8.0   | 11656 | 0.4509          | 0.1726 | 0.1668 | 0.2537 | 0.7463 | 55691 | 6401          | 2495      | 2251       | 0.1349 |
| 0.2947        | 9.0   | 13113 | 0.4550          | 0.1725 | 0.1667 | 0.2539 | 0.7461 | 55700 | 6426          | 2461      | 2257       | 0.1347 |
| 0.2892        | 10.0  | 14570 | 0.4586          | 0.1729 | 0.1671 | 0.2545 | 0.7455 | 55669 | 6448          | 2470      | 2249       | 0.1350 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
