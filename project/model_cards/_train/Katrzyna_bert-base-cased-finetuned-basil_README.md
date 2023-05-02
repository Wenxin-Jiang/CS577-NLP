---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: bert-base-cased-finetuned-basil
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-cased-finetuned-basil

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2272

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.8527        | 1.0   | 800  | 1.4425          |
| 1.4878        | 2.0   | 1600 | 1.2740          |
| 1.3776        | 3.0   | 2400 | 1.2273          |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Tokenizers 0.12.1
