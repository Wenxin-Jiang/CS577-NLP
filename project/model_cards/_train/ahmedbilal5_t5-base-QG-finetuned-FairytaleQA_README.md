---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- fairytale_qa
metrics:
- rouge
model-index:
- name: t5-base-QG-finetuned-FairytaleQA
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: fairytale_qa
      type: fairytale_qa
      config: default
      split: train
      args: default
    metrics:
    - name: Rouge1
      type: rouge
      value: 42.7529
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-QG-finetuned-FairytaleQA

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on the fairytale_qa dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1620
- Rouge1: 42.7529
- Rouge2: 23.9389
- Rougel: 40.4724
- Rougelsum: 40.4684
- Gen Len: 15.5698

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
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 1.4253        | 1.0   | 535  | 1.1620          | 42.7529 | 23.9389 | 40.4724 | 40.4684   | 15.5698 |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
