---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-8front-1body-8rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-8front-1body-8rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4376
- Wer: 0.1693
- Mer: 0.1635
- Wil: 0.2492
- Wip: 0.7508
- Hits: 55925
- Substitutions: 6304
- Deletions: 2358
- Insertions: 2270
- Cer: 0.1339

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
| 0.6093        | 1.0   | 1457  | 0.4649          | 0.2573 | 0.2324 | 0.3203 | 0.6797 | 54884 | 6813          | 2890      | 6916       | 0.2380 |
| 0.5049        | 2.0   | 2914  | 0.4186          | 0.1791 | 0.1722 | 0.2595 | 0.7405 | 55594 | 6456          | 2537      | 2575       | 0.1432 |
| 0.4746        | 3.0   | 4371  | 0.4147          | 0.1741 | 0.1681 | 0.2539 | 0.7461 | 55665 | 6315          | 2607      | 2324       | 0.1392 |
| 0.4295        | 4.0   | 5828  | 0.4118          | 0.1723 | 0.1661 | 0.2523 | 0.7477 | 55884 | 6360          | 2343      | 2425       | 0.1342 |
| 0.3881        | 5.0   | 7285  | 0.4123          | 0.1696 | 0.1639 | 0.2496 | 0.7504 | 55896 | 6301          | 2390      | 2265       | 0.1397 |
| 0.3151        | 6.0   | 8742  | 0.4174          | 0.1687 | 0.1631 | 0.2482 | 0.7518 | 55924 | 6249          | 2414      | 2236       | 0.1329 |
| 0.2977        | 7.0   | 10199 | 0.4248          | 0.1674 | 0.1618 | 0.2466 | 0.7534 | 56006 | 6227          | 2354      | 2229       | 0.1321 |
| 0.2737        | 8.0   | 11656 | 0.4293          | 0.1685 | 0.1629 | 0.2485 | 0.7515 | 55898 | 6288          | 2401      | 2192       | 0.1340 |
| 0.2574        | 9.0   | 13113 | 0.4374          | 0.1683 | 0.1627 | 0.2480 | 0.7520 | 55930 | 6268          | 2389      | 2212       | 0.1329 |
| 0.2472        | 10.0  | 14570 | 0.4376          | 0.1693 | 0.1635 | 0.2492 | 0.7508 | 55925 | 6304          | 2358      | 2270       | 0.1339 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
