---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-7front-1body-7rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-7front-1body-7rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4371
- Wer: 0.1693
- Mer: 0.1636
- Wil: 0.2493
- Wip: 0.7507
- Hits: 55894
- Substitutions: 6298
- Deletions: 2395
- Insertions: 2240
- Cer: 0.1325

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
| 0.6129        | 1.0   | 1457  | 0.4667          | 0.2078 | 0.1962 | 0.2857 | 0.7143 | 54967 | 6724          | 2896      | 3799       | 0.1785 |
| 0.5027        | 2.0   | 2914  | 0.4202          | 0.1767 | 0.1705 | 0.2573 | 0.7427 | 55529 | 6397          | 2661      | 2356       | 0.1393 |
| 0.486         | 3.0   | 4371  | 0.4128          | 0.1720 | 0.1667 | 0.2522 | 0.7478 | 55546 | 6265          | 2776      | 2068       | 0.1352 |
| 0.4381        | 4.0   | 5828  | 0.4077          | 0.1726 | 0.1664 | 0.2515 | 0.7485 | 55866 | 6263          | 2458      | 2427       | 0.1363 |
| 0.3859        | 5.0   | 7285  | 0.4151          | 0.1703 | 0.1644 | 0.2502 | 0.7498 | 55873 | 6310          | 2404      | 2282       | 0.1322 |
| 0.3091        | 6.0   | 8742  | 0.4172          | 0.1709 | 0.1649 | 0.2501 | 0.7499 | 55913 | 6267          | 2407      | 2365       | 0.1386 |
| 0.3012        | 7.0   | 10199 | 0.4258          | 0.1697 | 0.1637 | 0.2493 | 0.7507 | 55996 | 6304          | 2287      | 2369       | 0.1325 |
| 0.2837        | 8.0   | 11656 | 0.4275          | 0.1696 | 0.1639 | 0.2499 | 0.7501 | 55858 | 6325          | 2404      | 2222       | 0.1328 |
| 0.2625        | 9.0   | 13113 | 0.4339          | 0.1696 | 0.1639 | 0.2496 | 0.7504 | 55880 | 6296          | 2411      | 2248       | 0.1327 |
| 0.2466        | 10.0  | 14570 | 0.4371          | 0.1693 | 0.1636 | 0.2493 | 0.7507 | 55894 | 6298          | 2395      | 2240       | 0.1325 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
