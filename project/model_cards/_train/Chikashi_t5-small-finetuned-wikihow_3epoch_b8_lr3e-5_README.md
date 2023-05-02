---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wikihow
metrics:
- rouge
model-index:
- name: t5-small-finetuned-wikihow_3epoch_b8_lr3e-5
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
      value: 25.9411
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-wikihow_3epoch_b8_lr3e-5

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the wikihow dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4836
- Rouge1: 25.9411
- Rouge2: 9.226
- Rougel: 21.9087
- Rougelsum: 25.2863
- Gen Len: 18.4076

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| 2.912         | 0.25  | 5000  | 2.6285          | 23.6659 | 7.8535 | 19.9837 | 22.9884   | 18.3867 |
| 2.8115        | 0.51  | 10000 | 2.5820          | 24.7979 | 8.4888 | 20.8719 | 24.1321   | 18.3292 |
| 2.767         | 0.76  | 15000 | 2.5555          | 25.0857 | 8.6437 | 21.149  | 24.4256   | 18.2981 |
| 2.742         | 1.02  | 20000 | 2.5330          | 25.3431 | 8.8393 | 21.425  | 24.7032   | 18.3749 |
| 2.7092        | 1.27  | 25000 | 2.5203          | 25.5338 | 8.9281 | 21.5378 | 24.9045   | 18.3399 |
| 2.6989        | 1.53  | 30000 | 2.5065          | 25.4792 | 8.9745 | 21.4941 | 24.8458   | 18.4565 |
| 2.6894        | 1.78  | 35000 | 2.5018          | 25.6815 | 9.1218 | 21.6958 | 25.0557   | 18.406  |
| 2.6897        | 2.03  | 40000 | 2.4944          | 25.8241 | 9.2127 | 21.8205 | 25.1801   | 18.4228 |
| 2.6664        | 2.29  | 45000 | 2.4891          | 25.8241 | 9.1662 | 21.7807 | 25.1615   | 18.4258 |
| 2.6677        | 2.54  | 50000 | 2.4855          | 25.7435 | 9.145  | 21.765  | 25.0858   | 18.4329 |
| 2.6631        | 2.8   | 55000 | 2.4836          | 25.9411 | 9.226  | 21.9087 | 25.2863   | 18.4076 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
