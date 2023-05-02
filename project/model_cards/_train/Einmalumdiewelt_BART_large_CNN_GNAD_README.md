---
language:
- de
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: BART_large_CNN_GNAD
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BART_large_CNN_GNAD

This model is a fine-tuned version of [Einmalumdiewelt/BART_large_CNN_GNAD](https://huggingface.co/Einmalumdiewelt/BART_large_CNN_GNAD) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.9761
- Rouge1: 27.0918
- Rouge2: 7.9818
- Rougel: 17.7781
- Rougelsum: 22.6727
- Gen Len: 96.0567

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10.0

### Training results



### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
