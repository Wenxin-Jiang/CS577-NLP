---
license: mit
tags:
- generated_from_trainer
datasets:
- squad
model-index:
- name: roberta_checkpoint-finetuned-squad
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta_checkpoint-finetuned-squad

This model is a fine-tuned version of [WillHeld/roberta-base-coqa](https://huggingface.co/WillHeld/roberta-base-coqa) on the squad dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8934

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
| 0.8468        | 1.0   | 5536  | 0.8168          |
| 0.6239        | 2.0   | 11072 | 0.8237          |
| 0.4805        | 3.0   | 16608 | 0.8934          |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
