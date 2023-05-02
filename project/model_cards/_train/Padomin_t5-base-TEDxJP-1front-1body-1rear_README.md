---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-1front-1body-1rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-1front-1body-1rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4600
- Wer: 0.1742
- Mer: 0.1683
- Wil: 0.2562
- Wip: 0.7438
- Hits: 55625
- Substitutions: 6495
- Deletions: 2467
- Insertions: 2291
- Cer: 0.1364

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
| 0.6478        | 1.0   | 1457  | 0.4880          | 0.2256 | 0.2100 | 0.2999 | 0.7001 | 54825 | 6842          | 2920      | 4808       | 0.2019 |
| 0.542         | 2.0   | 2914  | 0.4461          | 0.1886 | 0.1807 | 0.2697 | 0.7303 | 55225 | 6615          | 2747      | 2817       | 0.1577 |
| 0.4873        | 3.0   | 4371  | 0.4390          | 0.1764 | 0.1702 | 0.2584 | 0.7416 | 55541 | 6519          | 2527      | 2344       | 0.1392 |
| 0.4271        | 4.0   | 5828  | 0.4361          | 0.1750 | 0.1691 | 0.2567 | 0.7433 | 55512 | 6453          | 2622      | 2226       | 0.1381 |
| 0.3705        | 5.0   | 7285  | 0.4366          | 0.1741 | 0.1684 | 0.2558 | 0.7442 | 55508 | 6427          | 2652      | 2164       | 0.1358 |
| 0.3557        | 6.0   | 8742  | 0.4424          | 0.1738 | 0.1679 | 0.2555 | 0.7445 | 55600 | 6453          | 2534      | 2235       | 0.1369 |
| 0.3838        | 7.0   | 10199 | 0.4471          | 0.1741 | 0.1684 | 0.2562 | 0.7438 | 55550 | 6473          | 2564      | 2210       | 0.1362 |
| 0.3095        | 8.0   | 11656 | 0.4517          | 0.1746 | 0.1685 | 0.2566 | 0.7434 | 55618 | 6499          | 2470      | 2305       | 0.1367 |
| 0.306         | 9.0   | 13113 | 0.4573          | 0.1748 | 0.1688 | 0.2570 | 0.7430 | 55601 | 6517          | 2469      | 2304       | 0.1369 |
| 0.3073        | 10.0  | 14570 | 0.4600          | 0.1742 | 0.1683 | 0.2562 | 0.7438 | 55625 | 6495          | 2467      | 2291       | 0.1364 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
