---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- samsum
metrics:
- rouge
model-index:
- name: t5-samsung-5e
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: samsum
      type: samsum
      config: samsum
      split: train
      args: samsum
    metrics:
    - name: Rouge1
      type: rouge
      value: 43.1484
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-samsung-5e

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the samsum dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7108
- Rouge1: 43.1484
- Rouge2: 20.4563
- Rougel: 36.6379
- Rougelsum: 40.196
- Gen Len: 16.7677

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 1.873         | 1.0   | 1841 | 1.7460          | 41.7428 | 19.2191 | 35.2428 | 38.8578   | 16.7286 |
| 1.8627        | 2.0   | 3682 | 1.7268          | 42.4494 | 19.8301 | 36.1459 | 39.5271   | 16.6039 |
| 1.8293        | 3.0   | 5523 | 1.7223          | 42.8908 | 19.9782 | 36.1848 | 39.8482   | 16.7164 |
| 1.8163        | 4.0   | 7364 | 1.7101          | 43.2291 | 20.3177 | 36.6418 | 40.2878   | 16.8472 |
| 1.8174        | 5.0   | 9205 | 1.7108          | 43.1484 | 20.4563 | 36.6379 | 40.196    | 16.7677 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
