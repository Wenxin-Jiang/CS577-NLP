---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased-finetuned-clinc
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-clinc

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7720
- Accuracy: 0.9184

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
- train_batch_size: 48
- eval_batch_size: 48
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 318  | 3.2891          | 0.7429   |
| 3.7868        | 2.0   | 636  | 1.8755          | 0.8374   |
| 3.7868        | 3.0   | 954  | 1.1570          | 0.8961   |
| 1.6928        | 4.0   | 1272 | 0.8573          | 0.9132   |
| 0.9056        | 5.0   | 1590 | 0.7720          | 0.9184   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Tokenizers 0.13.2
