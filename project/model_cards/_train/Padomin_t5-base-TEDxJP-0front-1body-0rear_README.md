---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-0front-1body-0rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-0front-1body-0rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5110
- Wer: 0.1852
- Mer: 0.1786
- Wil: 0.2694
- Wip: 0.7306
- Hits: 55023
- Substitutions: 6739
- Deletions: 2825
- Insertions: 2397
- Cer: 0.1459

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
| 0.6898        | 1.0   | 1457  | 0.5259          | 0.2378 | 0.2201 | 0.3112 | 0.6888 | 54412 | 6955          | 3220      | 5183       | 0.2118 |
| 0.5915        | 2.0   | 2914  | 0.4905          | 0.1893 | 0.1824 | 0.2734 | 0.7266 | 54815 | 6756          | 3016      | 2455       | 0.1588 |
| 0.5414        | 3.0   | 4371  | 0.4812          | 0.1933 | 0.1850 | 0.2748 | 0.7252 | 54989 | 6684          | 2914      | 2885       | 0.1605 |
| 0.4633        | 4.0   | 5828  | 0.4820          | 0.1847 | 0.1782 | 0.2685 | 0.7315 | 54999 | 6685          | 2903      | 2342       | 0.1451 |
| 0.4275        | 5.0   | 7285  | 0.4831          | 0.1851 | 0.1785 | 0.2681 | 0.7319 | 55034 | 6630          | 2923      | 2405       | 0.1491 |
| 0.3977        | 6.0   | 8742  | 0.4903          | 0.1836 | 0.1773 | 0.2676 | 0.7324 | 54996 | 6681          | 2910      | 2264       | 0.1451 |
| 0.4236        | 7.0   | 10199 | 0.4941          | 0.1853 | 0.1788 | 0.2693 | 0.7307 | 54964 | 6706          | 2917      | 2343       | 0.1451 |
| 0.3496        | 8.0   | 11656 | 0.5022          | 0.1861 | 0.1794 | 0.2693 | 0.7307 | 54979 | 6661          | 2947      | 2409       | 0.1516 |
| 0.3439        | 9.0   | 13113 | 0.5081          | 0.1872 | 0.1802 | 0.2709 | 0.7291 | 55016 | 6738          | 2833      | 2519       | 0.1606 |
| 0.3505        | 10.0  | 14570 | 0.5110          | 0.1852 | 0.1786 | 0.2694 | 0.7306 | 55023 | 6739          | 2825      | 2397       | 0.1459 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
