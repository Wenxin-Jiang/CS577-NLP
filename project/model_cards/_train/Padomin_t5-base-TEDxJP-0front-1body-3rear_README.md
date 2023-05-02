---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-0front-1body-3rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-0front-1body-3rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4700
- Wer: 0.1779
- Mer: 0.1718
- Wil: 0.2600
- Wip: 0.7400
- Hits: 55384
- Substitutions: 6510
- Deletions: 2693
- Insertions: 2287
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
| 0.6519        | 1.0   | 1457  | 0.4991          | 0.2099 | 0.1985 | 0.2891 | 0.7109 | 54721 | 6807          | 3059      | 3689       | 0.1855 |
| 0.5507        | 2.0   | 2914  | 0.4589          | 0.1827 | 0.1764 | 0.2653 | 0.7347 | 55094 | 6566          | 2927      | 2305       | 0.1504 |
| 0.5097        | 3.0   | 4371  | 0.4493          | 0.1797 | 0.1734 | 0.2615 | 0.7385 | 55330 | 6503          | 2754      | 2352       | 0.1428 |
| 0.4457        | 4.0   | 5828  | 0.4458          | 0.1757 | 0.1702 | 0.2581 | 0.7419 | 55319 | 6463          | 2805      | 2078       | 0.1376 |
| 0.3913        | 5.0   | 7285  | 0.4486          | 0.1774 | 0.1716 | 0.2600 | 0.7400 | 55324 | 6525          | 2738      | 2195       | 0.1414 |
| 0.3641        | 6.0   | 8742  | 0.4553          | 0.1764 | 0.1706 | 0.2595 | 0.7405 | 55397 | 6566          | 2624      | 2202       | 0.1378 |
| 0.4101        | 7.0   | 10199 | 0.4596          | 0.1770 | 0.1711 | 0.2596 | 0.7404 | 55360 | 6528          | 2699      | 2202       | 0.1387 |
| 0.3305        | 8.0   | 11656 | 0.4654          | 0.1783 | 0.1722 | 0.2606 | 0.7394 | 55358 | 6528          | 2701      | 2288       | 0.1393 |
| 0.317         | 9.0   | 13113 | 0.4671          | 0.1782 | 0.1720 | 0.2604 | 0.7396 | 55386 | 6524          | 2677      | 2307       | 0.1400 |
| 0.3232        | 10.0  | 14570 | 0.4700          | 0.1779 | 0.1718 | 0.2600 | 0.7400 | 55384 | 6510          | 2693      | 2287       | 0.1398 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
