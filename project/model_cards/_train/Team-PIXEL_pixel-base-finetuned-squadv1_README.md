---
tags:
- generated_from_trainer
datasets:
- squad
model-index:
- name: pixel-base-finetuned-squadv1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pixel-base-finetuned-squad-v1 

This model is a fine-tuned version of [Team-PIXEL/pixel-base](https://huggingface.co/Team-PIXEL/pixel-base) on the squad dataset.

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- training_steps: 20000
- mixed_precision_training: Apex, opt level O1

### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0
- Datasets 2.0.0
- Tokenizers 0.12.1
