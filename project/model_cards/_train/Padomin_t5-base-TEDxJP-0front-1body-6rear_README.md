---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-0front-1body-6rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-0front-1body-6rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4688
- Wer: 0.1755
- Mer: 0.1695
- Wil: 0.2577
- Wip: 0.7423
- Hits: 55504
- Substitutions: 6505
- Deletions: 2578
- Insertions: 2249
- Cer: 0.1373

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
| 0.6426        | 1.0   | 1457  | 0.4936          | 0.2128 | 0.2007 | 0.2903 | 0.7097 | 54742 | 6734          | 3111      | 3899       | 0.1791 |
| 0.5519        | 2.0   | 2914  | 0.4535          | 0.1970 | 0.1876 | 0.2747 | 0.7253 | 55096 | 6467          | 3024      | 3233       | 0.1567 |
| 0.5007        | 3.0   | 4371  | 0.4465          | 0.1819 | 0.1751 | 0.2628 | 0.7372 | 55359 | 6481          | 2747      | 2522       | 0.1435 |
| 0.4374        | 4.0   | 5828  | 0.4417          | 0.1761 | 0.1703 | 0.2582 | 0.7418 | 55399 | 6471          | 2717      | 2184       | 0.1373 |
| 0.3831        | 5.0   | 7285  | 0.4459          | 0.1755 | 0.1697 | 0.2570 | 0.7430 | 55465 | 6429          | 2693      | 2214       | 0.1383 |
| 0.352         | 6.0   | 8742  | 0.4496          | 0.1755 | 0.1697 | 0.2573 | 0.7427 | 55452 | 6450          | 2685      | 2202       | 0.1374 |
| 0.3955        | 7.0   | 10199 | 0.4527          | 0.1766 | 0.1707 | 0.2580 | 0.7420 | 55429 | 6429          | 2729      | 2251       | 0.1392 |
| 0.3132        | 8.0   | 11656 | 0.4629          | 0.1764 | 0.1703 | 0.2580 | 0.7420 | 55522 | 6472          | 2593      | 2329       | 0.1380 |
| 0.3116        | 9.0   | 13113 | 0.4652          | 0.1755 | 0.1695 | 0.2577 | 0.7423 | 55517 | 6505          | 2565      | 2264       | 0.1371 |
| 0.313         | 10.0  | 14570 | 0.4688          | 0.1755 | 0.1695 | 0.2577 | 0.7423 | 55504 | 6505          | 2578      | 2249       | 0.1373 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
