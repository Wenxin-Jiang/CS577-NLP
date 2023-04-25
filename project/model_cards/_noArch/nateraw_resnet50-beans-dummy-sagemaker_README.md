---
tags:
- image-classification
- timm
- generated_from_trainer
datasets:
- beans
model-index:
- name: model
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: beans
      type: beans
      args: default
library_tag: timm
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# model

This model is a fine-tuned version of [resnet18](https://huggingface.co/resnet18) on the beans dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0219
- Acc1: 56.3910
- Acc5: 100.0

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
- training_steps: 20

### Training results



### Framework versions

- Transformers 4.10.2
- Pytorch 1.7.1
- Datasets 1.12.1
- Tokenizers 0.10.3
