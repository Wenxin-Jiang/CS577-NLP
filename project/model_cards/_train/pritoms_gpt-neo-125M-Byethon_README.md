---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- null
model-index:
- name: gpt-neo-125M-Byethon
  results:
  - task:
      name: Causal Language Modeling
      type: text-generation
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt-neo-125M-Byethon

This model is a fine-tuned version of [EleutherAI/gpt-neo-125M](https://huggingface.co/EleutherAI/gpt-neo-125M) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6609

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 237  | 0.8348          |
| No log        | 2.0   | 474  | 0.6931          |
| 0.8151        | 3.0   | 711  | 0.6609          |


### Framework versions

- Transformers 4.10.2
- Pytorch 1.9.0+cu102
- Datasets 1.11.0
- Tokenizers 0.10.3
