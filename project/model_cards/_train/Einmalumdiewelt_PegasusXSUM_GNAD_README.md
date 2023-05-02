---
language:
- de
tags:
- generated_from_trainer
- summarization
metrics:
- rouge
model-index:
- name: PegasusXSUM_GNAD
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PegasusXSUM_GNAD

This model is a fine-tuned version of [Einmalumdiewelt/PegasusXSUM_GNAD](https://huggingface.co/Einmalumdiewelt/PegasusXSUM_GNAD) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4386
- Rouge1: 26.7818
- Rouge2: 7.6864
- Rougel: 18.6264
- Rougelsum: 22.822
- Gen Len: 67.076

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
- train_batch_size: 2
- eval_batch_size: 2
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
