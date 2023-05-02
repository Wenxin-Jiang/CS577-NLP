---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-0front-1body-5rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-0front-1body-5rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4695
- Wer: 0.1761
- Mer: 0.1701
- Wil: 0.2587
- Wip: 0.7413
- Hits: 55488
- Substitutions: 6549
- Deletions: 2550
- Insertions: 2272
- Cer: 0.1410

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
| 0.6479        | 1.0   | 1457  | 0.4975          | 0.1917 | 0.1845 | 0.2761 | 0.7239 | 54735 | 6812          | 3040      | 2530       | 0.1545 |
| 0.549         | 2.0   | 2914  | 0.4537          | 0.1833 | 0.1768 | 0.2659 | 0.7341 | 55124 | 6589          | 2874      | 2378       | 0.1435 |
| 0.4961        | 3.0   | 4371  | 0.4472          | 0.1758 | 0.1701 | 0.2582 | 0.7418 | 55387 | 6493          | 2707      | 2154       | 0.1369 |
| 0.432         | 4.0   | 5828  | 0.4439          | 0.1765 | 0.1707 | 0.2593 | 0.7407 | 55403 | 6544          | 2640      | 2217       | 0.1387 |
| 0.3789        | 5.0   | 7285  | 0.4471          | 0.1749 | 0.1693 | 0.2574 | 0.7426 | 55419 | 6490          | 2678      | 2128       | 0.1387 |
| 0.3524        | 6.0   | 8742  | 0.4483          | 0.1754 | 0.1697 | 0.2573 | 0.7427 | 55414 | 6449          | 2724      | 2153       | 0.1405 |
| 0.3961        | 7.0   | 10199 | 0.4562          | 0.1756 | 0.1698 | 0.2574 | 0.7426 | 55454 | 6455          | 2678      | 2206       | 0.1390 |
| 0.3238        | 8.0   | 11656 | 0.4593          | 0.1768 | 0.1708 | 0.2590 | 0.7410 | 55463 | 6514          | 2610      | 2298       | 0.1416 |
| 0.3054        | 9.0   | 13113 | 0.4652          | 0.1756 | 0.1697 | 0.2577 | 0.7423 | 55522 | 6498          | 2567      | 2279       | 0.1408 |
| 0.3087        | 10.0  | 14570 | 0.4695          | 0.1761 | 0.1701 | 0.2587 | 0.7413 | 55488 | 6549          | 2550      | 2272       | 0.1410 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
