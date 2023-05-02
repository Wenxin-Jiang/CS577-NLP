---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- eli5
metrics:
- rouge
model-index:
- name: t5-small-finetuned-eli5-extra-finetune
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
      value: 9.8647
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-eli5-extra-finetune

This model is a fine-tuned version of [Sandipan1994/t5-small-finetuned-eli5](https://huggingface.co/Sandipan1994/t5-small-finetuned-eli5) on the eli5 dataset.
It achieves the following results on the evaluation set:
- Loss: 3.6711
- Rouge1: 9.8647
- Rouge2: 1.9166
- Rougel: 7.9523
- Rougelsum: 9.1657
- Gen Len: 18.9981

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
| 3.8865        | 1.0   | 17040 | 3.6929          | 9.9257 | 1.9075 | 8.026  | 9.2238    | 19.0    |
| 3.8777        | 2.0   | 34080 | 3.6764          | 9.8568 | 1.9027 | 7.9443 | 9.1535    | 18.9981 |
| 3.8667        | 3.0   | 51120 | 3.6711          | 9.8647 | 1.9166 | 7.9523 | 9.1657    | 18.9981 |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1
