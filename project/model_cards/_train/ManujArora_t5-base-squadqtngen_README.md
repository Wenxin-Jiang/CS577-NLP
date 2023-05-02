---
license: apache-2.0
tags:
- question_generator
- generated_from_trainer
model-index:
- name: t5-base-squadqtngen
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-squadqtngen

This model is a fine-tuned version of [ManujArora/t5-base-squadqtngen](https://huggingface.co/ManujArora/t5-base-squadqtngen) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7049

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 248  | 1.6398          |
| No log        | 2.0   | 496  | 1.6440          |
| No log        | 3.0   | 744  | 1.6594          |
| No log        | 4.0   | 992  | 1.6720          |
| No log        | 5.0   | 1240 | 1.6824          |
| No log        | 6.0   | 1488 | 1.6949          |
| No log        | 7.0   | 1736 | 1.7032          |
| No log        | 8.0   | 1984 | 1.7049          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
