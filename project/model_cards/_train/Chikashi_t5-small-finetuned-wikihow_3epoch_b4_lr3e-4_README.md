---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wikihow
metrics:
- rouge
model-index:
- name: t5-small-finetuned-wikihow_3epoch_b4_lr3e-4
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: wikihow
      type: wikihow
      args: all
    metrics:
    - name: Rouge1
      type: rouge
      value: 27.4024
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-wikihow_3epoch_b4_lr3e-4

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the wikihow dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2757
- Rouge1: 27.4024
- Rouge2: 10.7065
- Rougel: 23.3153
- Rougelsum: 26.7336
- Gen Len: 18.5506

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step   | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:------:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 2.8424        | 0.13  | 5000   | 2.5695          | 25.2232 | 8.7617  | 21.2019 | 24.4949   | 18.4151 |
| 2.7334        | 0.25  | 10000  | 2.5229          | 25.3739 | 9.0477  | 21.5054 | 24.7553   | 18.3802 |
| 2.6823        | 0.38  | 15000  | 2.4857          | 26.341  | 9.6711  | 22.3446 | 25.7256   | 18.449  |
| 2.6607        | 0.51  | 20000  | 2.4540          | 26.0269 | 9.4722  | 22.0822 | 25.3602   | 18.4704 |
| 2.6137        | 0.64  | 25000  | 2.4326          | 26.2966 | 9.6815  | 22.4422 | 25.6326   | 18.3517 |
| 2.6077        | 0.76  | 30000  | 2.4108          | 26.0981 | 9.6221  | 22.1189 | 25.454    | 18.5079 |
| 2.5847        | 0.89  | 35000  | 2.3879          | 26.2675 | 9.6435  | 22.3738 | 25.6122   | 18.4838 |
| 2.5558        | 1.02  | 40000  | 2.3827          | 26.3458 | 9.7844  | 22.4718 | 25.7388   | 18.5097 |
| 2.4902        | 1.14  | 45000  | 2.3725          | 26.4987 | 9.9634  | 22.5398 | 25.8399   | 18.5912 |
| 2.4785        | 1.27  | 50000  | 2.3549          | 26.884  | 10.1136 | 22.8212 | 26.2262   | 18.4763 |
| 2.4822        | 1.4   | 55000  | 2.3467          | 26.8635 | 10.2266 | 22.9161 | 26.2252   | 18.5847 |
| 2.46          | 1.53  | 60000  | 2.3393          | 26.8602 | 10.1785 | 22.8453 | 26.1917   | 18.548  |
| 2.4523        | 1.65  | 65000  | 2.3330          | 26.91   | 10.237  | 22.9309 | 26.2372   | 18.5154 |
| 2.4525        | 1.78  | 70000  | 2.3203          | 27.073  | 10.4317 | 23.1355 | 26.4528   | 18.5063 |
| 2.4566        | 1.91  | 75000  | 2.3109          | 27.3853 | 10.5413 | 23.3455 | 26.7408   | 18.5258 |
| 2.4234        | 2.03  | 80000  | 2.3103          | 27.0836 | 10.4857 | 23.0538 | 26.409    | 18.5326 |
| 2.3686        | 2.16  | 85000  | 2.2986          | 27.311  | 10.6038 | 23.3068 | 26.6636   | 18.4874 |
| 2.3758        | 2.29  | 90000  | 2.2969          | 27.3509 | 10.6502 | 23.2764 | 26.6832   | 18.5438 |
| 2.3777        | 2.42  | 95000  | 2.2907          | 27.39   | 10.5842 | 23.3601 | 26.7433   | 18.5444 |
| 2.3624        | 2.54  | 100000 | 2.2875          | 27.3717 | 10.6098 | 23.3326 | 26.7232   | 18.5521 |
| 2.3543        | 2.67  | 105000 | 2.2811          | 27.4188 | 10.6919 | 23.3022 | 26.7426   | 18.564  |
| 2.366         | 2.8   | 110000 | 2.2763          | 27.4872 | 10.7079 | 23.4135 | 26.829    | 18.5399 |
| 2.3565        | 2.93  | 115000 | 2.2757          | 27.4024 | 10.7065 | 23.3153 | 26.7336   | 18.5506 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
