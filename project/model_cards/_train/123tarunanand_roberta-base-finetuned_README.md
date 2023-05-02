---
license: mit
tags:
- generated_from_trainer
datasets:
- squad_v2
model-index:
- name: roberta-base-finetuned-squad2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-finetuned-squad2

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the squad_v2 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9325

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.88          | 1.0   | 8160  | 0.8129          |
| 0.6643        | 2.0   | 16320 | 0.8567          |
| 0.5096        | 3.0   | 24480 | 0.9325          |


### Framework versions

- Transformers 4.12.2
- Pytorch 1.9.0+cu111
- Datasets 1.14.0
- Tokenizers 0.10.3
