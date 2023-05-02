---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: byt5small-glue-mprc2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# byt5small-glue-mprc2

This model is a fine-tuned version of [google/byt5-small](https://huggingface.co/google/byt5-small) on an unknown dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- distributed_type: tpu
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results



### Framework versions

- Transformers 4.18.0.dev0
- Pytorch 1.6.0a0+bf2bbd9
- Datasets 1.12.1
- Tokenizers 0.11.6
