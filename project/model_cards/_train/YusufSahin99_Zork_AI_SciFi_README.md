---
license: mit
tags:
- generated_from_trainer
model_index:
- name: Zork_AI_SciFi
  results:
  - task:
      name: Causal Language Modeling
      type: text-generation
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Zork_AI_SciFi

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on an unkown dataset.

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
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 200
- num_epochs: 3

### Training results



### Framework versions

- Transformers 4.8.2
- Pytorch 1.9.0+cu102
- Tokenizers 0.10.3
