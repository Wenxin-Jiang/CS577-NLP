---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: mbti-classification-roberta-base
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbti-classification-roberta-base

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1673
- Accuracy: 0.3031

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
- lr_scheduler_type: cosine
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step   | Validation Loss | Accuracy |
|:-------------:|:-----:|:------:|:---------------:|:--------:|
| 2.1161        | 1.0   | 20490  | 2.0814          | 0.2993   |
| 2.0021        | 2.0   | 40980  | 2.0563          | 0.3073   |
| 1.8974        | 3.0   | 61470  | 2.0769          | 0.3074   |
| 1.8346        | 4.0   | 81960  | 2.1221          | 0.3073   |
| 1.7826        | 5.0   | 102450 | 2.1673          | 0.3031   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu102
- Datasets 2.7.1
- Tokenizers 0.13.2
