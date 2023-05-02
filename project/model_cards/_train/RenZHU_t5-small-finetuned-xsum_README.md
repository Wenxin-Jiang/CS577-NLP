---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-small-finetuned-xsum
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-xsum

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.5310
- Rouge1: 27.9232
- Rouge2: 7.5324
- Rougel: 22.035
- Rougelsum: 22.0304
- Gen Len: 18.8116

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2 | Rougel | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:------:|:------:|:---------:|:-------:|
| 2.7564        | 1.0   | 51012 | 2.5310          | 27.9232 | 7.5324 | 22.035 | 22.0304   | 18.8116 |


### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.0+cu111
- Datasets 1.17.1.dev0
- Tokenizers 0.11.0
