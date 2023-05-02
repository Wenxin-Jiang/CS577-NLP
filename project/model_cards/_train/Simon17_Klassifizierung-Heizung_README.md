---
license: mit
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: Klassifizierung-Heizung
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Klassifizierung-Heizung

This model is a fine-tuned version of [bert-base-german-cased](https://huggingface.co/bert-base-german-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0936
- F1: 0.9859

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.7465        | 1.0   | 142  | 0.1972          | 0.9286 |
| 0.1416        | 2.0   | 284  | 0.1080          | 0.9859 |
| 0.0541        | 3.0   | 426  | 0.0936          | 0.9859 |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1
