---
tags:
- generated_from_trainer
model-index:
- name: roberta-retrained_ru_covid
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-retrained_ru_covid

This model is a fine-tuned version of [blinoff/roberta-base-russian-v0](https://huggingface.co/blinoff/roberta-base-russian-v0) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8518

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
- seed: 1
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 25

### Training results



### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
