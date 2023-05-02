---
language: zh
widget: 
- text: "这句话是谁说的？"
  context: "“老大，你太牛逼了，把敌人军火库都给炸了，我真的佩服的五体投地，我现在忍不住想看看你藏的东西在哪里，我们快点出发吧。”代号零听完郭旭刚刚的讲述笑的拍手一直叫好。"
tags:
- generated_from_trainer
model-index:
- name: bert-finetuned-ViolentSmallFarmers
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ViolentSmallFarmers

This model is a fine-tuned version of [bert-base-chinese](https://huggingface.co/bert-base-chinese) on an unknown dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results
exact_match：92.55702280912365
f1：92.55702280912365


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1
- Datasets 2.7.1
- Tokenizers 0.13.2
