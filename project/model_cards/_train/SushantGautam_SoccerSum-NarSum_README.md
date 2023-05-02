---
language:
- en
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: SportsSum
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# SportsSum

This model is a fine-tuned version of [allenai/led-base-16384-ms2](https://huggingface.co/allenai/led-base-16384-ms2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2759
- Rouge1: 52.3608
- Rouge2: 27.6526
- Rougel: 31.8509
- Rougelsum: 49.9086
- Gen Len: 248.1199

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 36
- eval_batch_size: 36
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10.0

### Training results



### Framework versions

- Transformers 4.21.0.dev0
- Pytorch 1.9.0+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1
