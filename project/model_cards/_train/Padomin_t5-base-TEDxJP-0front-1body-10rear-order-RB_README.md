---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-0front-1body-10rear-order-RB
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-0front-1body-10rear-order-RB

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4749
- Wer: 0.1754
- Mer: 0.1696
- Wil: 0.2575
- Wip: 0.7425
- Hits: 55482
- Substitutions: 6478
- Deletions: 2627
- Insertions: 2225
- Cer: 0.1370

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
| 0.637         | 1.0   | 1457  | 0.4932          | 0.2359 | 0.2179 | 0.3082 | 0.6918 | 54682 | 6909          | 2996      | 5331       | 0.2100 |
| 0.5501        | 2.0   | 2914  | 0.4572          | 0.1831 | 0.1766 | 0.2655 | 0.7345 | 55134 | 6575          | 2878      | 2370       | 0.1461 |
| 0.5505        | 3.0   | 4371  | 0.4470          | 0.1787 | 0.1728 | 0.2609 | 0.7391 | 55267 | 6494          | 2826      | 2222       | 0.1400 |
| 0.4921        | 4.0   | 5828  | 0.4426          | 0.1794 | 0.1730 | 0.2606 | 0.7394 | 55420 | 6468          | 2699      | 2423       | 0.1407 |
| 0.4465        | 5.0   | 7285  | 0.4507          | 0.1783 | 0.1721 | 0.2596 | 0.7404 | 55420 | 6458          | 2709      | 2351       | 0.1390 |
| 0.3557        | 6.0   | 8742  | 0.4567          | 0.1768 | 0.1708 | 0.2585 | 0.7415 | 55416 | 6459          | 2712      | 2245       | 0.1401 |
| 0.3367        | 7.0   | 10199 | 0.4613          | 0.1772 | 0.1709 | 0.2589 | 0.7411 | 55505 | 6497          | 2585      | 2363       | 0.1387 |
| 0.328         | 8.0   | 11656 | 0.4624          | 0.1769 | 0.1708 | 0.2587 | 0.7413 | 55442 | 6478          | 2667      | 2278       | 0.1383 |
| 0.2992        | 9.0   | 13113 | 0.4726          | 0.1764 | 0.1704 | 0.2580 | 0.7420 | 55461 | 6463          | 2663      | 2264       | 0.1378 |
| 0.2925        | 10.0  | 14570 | 0.4749          | 0.1754 | 0.1696 | 0.2575 | 0.7425 | 55482 | 6478          | 2627      | 2225       | 0.1370 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
