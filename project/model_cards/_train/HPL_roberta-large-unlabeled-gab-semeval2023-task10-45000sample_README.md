---
license: mit
tags:
- generated_from_trainer
model-index:
- name: roberta-large-unlabeled-gab-semeval2023-task10-45000sample
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-large-unlabeled-gab-semeval2023-task10-45000sample

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8859

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.1552        | 1.0   | 1407 | 1.9502          |
| 1.9918        | 2.0   | 2814 | 1.8859          |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.10.3
