---
license: mit
tags:
- generated_from_trainer
model-index:
- name: output
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on a dataset of Shakespeare's plays.

## Model description

The model is the original gpt-2 model fine-tuned on a custom dataset.

## Intended uses & limitations

The model can be used to generate Shakespearean-like text. Consider that because it comes from plays, such a typographical structure might be reproduced.

## Training and evaluation data

Trained with Shakespeare's plays corpus.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2.0

### Training results



### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.0+cu111
- Datasets 1.18.0
- Tokenizers 0.11.0
