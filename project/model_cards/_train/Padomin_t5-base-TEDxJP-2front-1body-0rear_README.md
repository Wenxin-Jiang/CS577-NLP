---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-2front-1body-0rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-2front-1body-0rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4717
- Wer: 0.1762
- Mer: 0.1701
- Wil: 0.2575
- Wip: 0.7425
- Hits: 55549
- Substitutions: 6453
- Deletions: 2585
- Insertions: 2345
- Cer: 0.1398

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
| 0.6666        | 1.0   | 1457  | 0.5030          | 0.2075 | 0.1970 | 0.2883 | 0.7117 | 54622 | 6855          | 3110      | 3434       | 0.1720 |
| 0.567         | 2.0   | 2914  | 0.4611          | 0.1950 | 0.1859 | 0.2750 | 0.7250 | 55142 | 6648          | 2797      | 3148       | 0.1598 |
| 0.5029        | 3.0   | 4371  | 0.4463          | 0.1832 | 0.1762 | 0.2640 | 0.7360 | 55317 | 6492          | 2778      | 2564       | 0.1445 |
| 0.443         | 4.0   | 5828  | 0.4452          | 0.1791 | 0.1728 | 0.2606 | 0.7394 | 55375 | 6482          | 2730      | 2354       | 0.1408 |
| 0.3979        | 5.0   | 7285  | 0.4473          | 0.1782 | 0.1719 | 0.2592 | 0.7408 | 55434 | 6438          | 2715      | 2355       | 0.1400 |
| 0.3745        | 6.0   | 8742  | 0.4521          | 0.1757 | 0.1698 | 0.2573 | 0.7427 | 55501 | 6450          | 2636      | 2264       | 0.1373 |
| 0.3889        | 7.0   | 10199 | 0.4572          | 0.1775 | 0.1713 | 0.2586 | 0.7414 | 55458 | 6438          | 2691      | 2334       | 0.1398 |
| 0.3247        | 8.0   | 11656 | 0.4650          | 0.1752 | 0.1693 | 0.2564 | 0.7436 | 55516 | 6409          | 2662      | 2245       | 0.1372 |
| 0.3207        | 9.0   | 13113 | 0.4693          | 0.1766 | 0.1703 | 0.2580 | 0.7420 | 55549 | 6474          | 2564      | 2367       | 0.1400 |
| 0.3264        | 10.0  | 14570 | 0.4717          | 0.1762 | 0.1701 | 0.2575 | 0.7425 | 55549 | 6453          | 2585      | 2345       | 0.1398 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
