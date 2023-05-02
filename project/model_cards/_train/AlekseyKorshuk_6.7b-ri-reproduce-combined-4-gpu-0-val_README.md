---
license: other
tags:
- generated_from_trainer
datasets:
- ChaiML/dalio_combined_v1
model-index:
- name: 6.7b-ri-reproduce-combined-4-gpu-0-val
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 6.7b-ri-reproduce-combined-4-gpu-0-val

This model is a fine-tuned version of [facebook/opt-6.7b](https://huggingface.co/facebook/opt-6.7b) on the ChaiML/dalio_combined_v1 dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 9e-07
- train_batch_size: 1
- eval_batch_size: 8
- seed: 100
- distributed_type: multi-GPU
- num_devices: 4
- total_train_batch_size: 4
- total_eval_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: constant
- num_epochs: 15.0

### Training results



### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
