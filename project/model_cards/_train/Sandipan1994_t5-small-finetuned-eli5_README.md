---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- eli5
metrics:
- rouge
model-index:
- name: t5-small-finetuned-eli5
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: eli5
      type: eli5
      config: LFQA_reddit
      split: train_eli5
      args: LFQA_reddit
    metrics:
    - name: Rouge1
      type: rouge
      value: 9.944
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-eli5

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the eli5 dataset.
It achieves the following results on the evaluation set:
- Loss: 3.7275
- Rouge1: 9.944
- Rouge2: 1.908
- Rougel: 8.0145
- Rougelsum: 9.2275
- Gen Len: 18.9988

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

| Training Loss | Epoch | Step  | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:------:|:---------:|:-------:|
| 3.9806        | 1.0   | 17040 | 3.7726          | 9.8475 | 1.872  | 7.9462 | 9.1258    | 18.9972 |
| 3.9458        | 2.0   | 34080 | 3.7369          | 9.9232 | 1.8981 | 7.9922 | 9.2061    | 18.9988 |
| 3.9355        | 3.0   | 51120 | 3.7275          | 9.944  | 1.908  | 8.0145 | 9.2275    | 18.9988 |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1
