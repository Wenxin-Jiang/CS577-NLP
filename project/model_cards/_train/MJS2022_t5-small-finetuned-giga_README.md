---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- gigaword
metrics:
- rouge
model-index:
- name: t5-small-finetuned-giga
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: gigaword
      type: gigaword
      config: default
      split: train[:10%]
      args: default
    metrics:
    - name: Rouge1
      type: rouge
      value: 26.6579
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-giga

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the gigaword dataset.
It achieves the following results on the evaluation set:
- Loss: 3.2594
- Rouge1: 26.6579
- Rouge2: 9.5505
- Rougel: 24.4987
- Rougelsum: 24.5146
- Gen Len: 13.5436

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

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| 1.8512        | 1.0   | 23775 | 3.2594          | 26.6579 | 9.5505 | 24.4987 | 24.5146   | 13.5436 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
