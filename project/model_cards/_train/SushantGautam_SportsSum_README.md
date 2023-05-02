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
- Loss: 1.5344
- Rouge1: 55.5224
- Rouge2: 28.1394
- Rougel: 31.9521
- Rougelsum: 53.0848
- Gen Len: 312.3902

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
- train_batch_size: 96
- eval_batch_size: 96
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20.0

### Training results



### Framework versions

- Transformers 4.21.0.dev0
- Pytorch 1.9.0+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1
