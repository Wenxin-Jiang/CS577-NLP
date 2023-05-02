---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-5front-1body-5rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-5front-1body-5rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4383
- Wer: 0.1697
- Mer: 0.1641
- Wil: 0.2500
- Wip: 0.7500
- Hits: 55852
- Substitutions: 6314
- Deletions: 2421
- Insertions: 2228
- Cer: 0.1328

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
| 0.6185        | 1.0   | 1457  | 0.4683          | 0.1948 | 0.1863 | 0.2758 | 0.7242 | 54959 | 6658          | 2970      | 2956       | 0.1682 |
| 0.5149        | 2.0   | 2914  | 0.4280          | 0.1773 | 0.1713 | 0.2591 | 0.7409 | 55376 | 6468          | 2743      | 2238       | 0.1426 |
| 0.4705        | 3.0   | 4371  | 0.4173          | 0.1743 | 0.1682 | 0.2552 | 0.7448 | 55680 | 6418          | 2489      | 2351       | 0.1387 |
| 0.4023        | 4.0   | 5828  | 0.4114          | 0.1713 | 0.1656 | 0.2515 | 0.7485 | 55751 | 6313          | 2523      | 2230       | 0.1335 |
| 0.3497        | 5.0   | 7285  | 0.4162          | 0.1722 | 0.1662 | 0.2522 | 0.7478 | 55787 | 6331          | 2469      | 2323       | 0.1365 |
| 0.3246        | 6.0   | 8742  | 0.4211          | 0.1714 | 0.1655 | 0.2513 | 0.7487 | 55802 | 6310          | 2475      | 2284       | 0.1367 |
| 0.3492        | 7.0   | 10199 | 0.4282          | 0.1711 | 0.1652 | 0.2514 | 0.7486 | 55861 | 6350          | 2376      | 2325       | 0.1341 |
| 0.2788        | 8.0   | 11656 | 0.4322          | 0.1698 | 0.1641 | 0.2502 | 0.7498 | 55883 | 6342          | 2362      | 2265       | 0.1327 |
| 0.2801        | 9.0   | 13113 | 0.4362          | 0.1710 | 0.1652 | 0.2514 | 0.7486 | 55828 | 6351          | 2408      | 2288       | 0.1352 |
| 0.2773        | 10.0  | 14570 | 0.4383          | 0.1697 | 0.1641 | 0.2500 | 0.7500 | 55852 | 6314          | 2421      | 2228       | 0.1328 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
