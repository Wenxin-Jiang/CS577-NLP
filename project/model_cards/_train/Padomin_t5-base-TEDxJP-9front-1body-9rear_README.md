---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-9front-1body-9rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-9front-1body-9rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4361
- Wer: 0.1687
- Mer: 0.1630
- Wil: 0.2486
- Wip: 0.7514
- Hits: 55941
- Substitutions: 6292
- Deletions: 2354
- Insertions: 2252
- Cer: 0.1338

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
| 0.6124        | 1.0   | 1457  | 0.4613          | 0.2407 | 0.2209 | 0.3091 | 0.6909 | 54843 | 6758          | 2986      | 5804       | 0.2153 |
| 0.4968        | 2.0   | 2914  | 0.4171          | 0.1777 | 0.1716 | 0.2580 | 0.7420 | 55404 | 6354          | 2829      | 2293       | 0.1402 |
| 0.4817        | 3.0   | 4371  | 0.4129          | 0.1731 | 0.1673 | 0.2534 | 0.7466 | 55636 | 6332          | 2619      | 2227       | 0.1349 |
| 0.4257        | 4.0   | 5828  | 0.4089          | 0.1722 | 0.1659 | 0.2520 | 0.7480 | 55904 | 6346          | 2337      | 2437       | 0.1361 |
| 0.3831        | 5.0   | 7285  | 0.4144          | 0.1705 | 0.1646 | 0.2508 | 0.7492 | 55868 | 6343          | 2376      | 2290       | 0.1358 |
| 0.3057        | 6.0   | 8742  | 0.4198          | 0.1690 | 0.1632 | 0.2492 | 0.7508 | 55972 | 6333          | 2282      | 2298       | 0.1350 |
| 0.2919        | 7.0   | 10199 | 0.4220          | 0.1693 | 0.1635 | 0.2492 | 0.7508 | 55936 | 6310          | 2341      | 2281       | 0.1337 |
| 0.2712        | 8.0   | 11656 | 0.4252          | 0.1688 | 0.1632 | 0.2487 | 0.7513 | 55905 | 6286          | 2396      | 2218       | 0.1348 |
| 0.2504        | 9.0   | 13113 | 0.4332          | 0.1685 | 0.1629 | 0.2482 | 0.7518 | 55931 | 6270          | 2386      | 2226       | 0.1331 |
| 0.2446        | 10.0  | 14570 | 0.4361          | 0.1687 | 0.1630 | 0.2486 | 0.7514 | 55941 | 6292          | 2354      | 2252       | 0.1338 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
