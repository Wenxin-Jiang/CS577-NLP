---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-6front-1body-0rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-6front-1body-0rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4613
- Wer: 0.1753
- Mer: 0.1692
- Wil: 0.2565
- Wip: 0.7435
- Hits: 55602
- Substitutions: 6443
- Deletions: 2542
- Insertions: 2338
- Cer: 0.1381

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
| 0.6523        | 1.0   | 1457  | 0.4912          | 0.2014 | 0.1921 | 0.2829 | 0.7171 | 54699 | 6782          | 3106      | 3118       | 0.1699 |
| 0.5429        | 2.0   | 2914  | 0.4424          | 0.1879 | 0.1801 | 0.2682 | 0.7318 | 55234 | 6529          | 2824      | 2782       | 0.1505 |
| 0.4888        | 3.0   | 4371  | 0.4371          | 0.1761 | 0.1699 | 0.2567 | 0.7433 | 55564 | 6391          | 2632      | 2353       | 0.1376 |
| 0.4287        | 4.0   | 5828  | 0.4328          | 0.1738 | 0.1680 | 0.2542 | 0.7458 | 55584 | 6332          | 2671      | 2223       | 0.1350 |
| 0.387         | 5.0   | 7285  | 0.4357          | 0.1747 | 0.1687 | 0.2555 | 0.7445 | 55627 | 6399          | 2561      | 2326       | 0.1360 |
| 0.3497        | 6.0   | 8742  | 0.4405          | 0.1750 | 0.1690 | 0.2558 | 0.7442 | 55587 | 6399          | 2601      | 2301       | 0.1370 |
| 0.3703        | 7.0   | 10199 | 0.4480          | 0.1748 | 0.1689 | 0.2560 | 0.7440 | 55554 | 6416          | 2617      | 2258       | 0.1363 |
| 0.3038        | 8.0   | 11656 | 0.4542          | 0.1746 | 0.1686 | 0.2554 | 0.7446 | 55638 | 6399          | 2550      | 2331       | 0.1369 |
| 0.3045        | 9.0   | 13113 | 0.4574          | 0.1752 | 0.1691 | 0.2564 | 0.7436 | 55596 | 6441          | 2550      | 2324       | 0.1381 |
| 0.3008        | 10.0  | 14570 | 0.4613          | 0.1753 | 0.1692 | 0.2565 | 0.7435 | 55602 | 6443          | 2542      | 2338       | 0.1381 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
