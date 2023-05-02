---
license: mit
tags:
- generated_from_trainer
model-index:
- name: roberta-large-unlabeled-gab-reddit-semeval2023-task10-57000sample
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-large-unlabeled-gab-reddit-semeval2023-task10-57000sample

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8874

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
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 2.1999        | 1.0   | 3563  | 2.0576          |
| 2.0587        | 2.0   | 7126  | 1.9371          |
| 1.9591        | 3.0   | 10689 | 1.8823          |
| 1.8652        | 4.0   | 14252 | 1.8874          |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.0
- Tokenizers 0.10.3
