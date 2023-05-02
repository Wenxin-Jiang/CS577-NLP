---
license: cc-by-nc-sa-4.0
tags:
- generated_from_trainer
model-index:
- name: layoutlmv2-finetuned-funsd-test
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutlmv2-finetuned-funsd-test

This model is a fine-tuned version of [microsoft/layoutlmv2-base-uncased](https://huggingface.co/microsoft/layoutlmv2-base-uncased) on an unknown dataset.

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
- lr_scheduler_warmup_ratio: 0.1
- training_steps: 1000
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.8.0+cu101
- Datasets 2.2.2
- Tokenizers 0.12.1