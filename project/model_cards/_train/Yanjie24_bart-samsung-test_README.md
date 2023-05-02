---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- samsum
metrics:
- rouge
model-index:
- name: bart-samsung-test
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
      value: 46.7195
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-samsung-test

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on the samsum dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5511
- Rouge1: 46.7195
- Rouge2: 23.3711
- Rougel: 39.5121
- Rougelsum: 43.2091
- Gen Len: 17.7738

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
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 1.6838        | 1.0   | 1841 | 1.5511          | 46.7195 | 23.3711 | 39.5121 | 43.2091   | 17.7738 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
