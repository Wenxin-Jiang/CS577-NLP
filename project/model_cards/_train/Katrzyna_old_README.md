---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: bert-base-uncased-finetuned-basil
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-basil

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2870

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
| 1.9097        | 1.0   | 780  | 1.4978          |
| 1.5358        | 2.0   | 1560 | 1.3439          |
| 1.4259        | 3.0   | 2340 | 1.2881          |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Tokenizers 0.12.1
