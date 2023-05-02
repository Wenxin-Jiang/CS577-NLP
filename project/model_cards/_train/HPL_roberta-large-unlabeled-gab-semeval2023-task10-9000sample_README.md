---
license: mit
tags:
- generated_from_trainer
model-index:
- name: roberta-large-unlabeled-gab-semeval2023-task10-9000sample
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-large-unlabeled-gab-semeval2023-task10-9000sample

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0541

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.515         | 1.0   | 563  | 2.3288          |
| 2.2807        | 2.0   | 1126 | 2.1769          |
| 2.0351        | 3.0   | 1689 | 2.0541          |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.10.3
