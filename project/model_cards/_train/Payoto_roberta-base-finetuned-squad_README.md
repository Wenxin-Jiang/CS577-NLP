---
license: mit
tags:
- generated_from_trainer
datasets:
- squad
model-index:
- name: roberta-base-finetuned-squad
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-finetuned-squad

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the squad dataset.

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: IPU
- gradient_accumulation_steps: 32
- total_train_batch_size: 128
- total_eval_batch_size: 20
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.25
- num_epochs: 3
- training precision: Mixed Precision

### Training results



### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.0+cpu
- Datasets 2.7.1
- Tokenizers 0.12.1
