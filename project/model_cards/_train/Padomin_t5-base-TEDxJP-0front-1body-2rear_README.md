---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-0front-1body-2rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-0front-1body-2rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4789
- Wer: 0.1778
- Mer: 0.1717
- Wil: 0.2602
- Wip: 0.7398
- Hits: 55410
- Substitutions: 6542
- Deletions: 2635
- Insertions: 2306
- Cer: 0.1406

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
| 0.6615        | 1.0   | 1457  | 0.5044          | 0.2284 | 0.2125 | 0.3029 | 0.6971 | 54662 | 6871          | 3054      | 4826       | 0.1972 |
| 0.5561        | 2.0   | 2914  | 0.4658          | 0.1850 | 0.1783 | 0.2672 | 0.7328 | 55088 | 6583          | 2916      | 2451       | 0.1484 |
| 0.5114        | 3.0   | 4371  | 0.4555          | 0.1813 | 0.1748 | 0.2624 | 0.7376 | 55272 | 6463          | 2852      | 2392       | 0.1454 |
| 0.4419        | 4.0   | 5828  | 0.4542          | 0.1801 | 0.1737 | 0.2621 | 0.7379 | 55326 | 6529          | 2732      | 2372       | 0.1418 |
| 0.3992        | 5.0   | 7285  | 0.4541          | 0.1786 | 0.1725 | 0.2609 | 0.7391 | 55329 | 6527          | 2731      | 2276       | 0.1403 |
| 0.3649        | 6.0   | 8742  | 0.4598          | 0.1769 | 0.1710 | 0.2596 | 0.7404 | 55401 | 6540          | 2646      | 2239       | 0.1386 |
| 0.399         | 7.0   | 10199 | 0.4653          | 0.1786 | 0.1725 | 0.2610 | 0.7390 | 55327 | 6534          | 2726      | 2276       | 0.1414 |
| 0.3348        | 8.0   | 11656 | 0.4712          | 0.1784 | 0.1722 | 0.2611 | 0.7389 | 55391 | 6569          | 2627      | 2327       | 0.1409 |
| 0.3221        | 9.0   | 13113 | 0.4762          | 0.1782 | 0.1720 | 0.2608 | 0.7392 | 55404 | 6563          | 2620      | 2325       | 0.1408 |
| 0.3292        | 10.0  | 14570 | 0.4789          | 0.1778 | 0.1717 | 0.2602 | 0.7398 | 55410 | 6542          | 2635      | 2306       | 0.1406 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
