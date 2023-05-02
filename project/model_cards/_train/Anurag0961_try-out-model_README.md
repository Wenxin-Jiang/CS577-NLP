---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: try-out-model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# try-out-model

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0210
- F1: 0.8037

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
- train_batch_size: 12
- eval_batch_size: 12
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.1006        | 1.0   | 188  | 2.4095          | 0.4504 |
| 1.9221        | 2.0   | 376  | 1.5023          | 0.7072 |
| 1.2765        | 3.0   | 564  | 1.1263          | 0.7895 |
| 0.9936        | 4.0   | 752  | 1.0210          | 0.8037 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Tokenizers 0.13.2
