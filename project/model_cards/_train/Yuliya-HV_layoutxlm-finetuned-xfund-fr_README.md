---
license: cc-by-nc-sa-4.0
tags:
- generated_from_trainer
datasets:
- xfun
model-index:
- name: layoutxlm-finetuned-xfund-fr
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutxlm-finetuned-xfund-fr

This model is a fine-tuned version of [microsoft/layoutxlm-base](https://huggingface.co/microsoft/layoutxlm-base) on the xfun dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- training_steps: 1000

### Training results



### Framework versions

- Transformers 4.22.2
- Pytorch 1.10.0+cu111
- Datasets 2.5.2
- Tokenizers 0.12.1
