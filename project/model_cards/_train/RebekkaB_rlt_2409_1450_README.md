---
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: rlt_2409_1450
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# rlt_2409_1450

This model is a fine-tuned version of [svalabs/gbert-large-zeroshot-nli](https://huggingface.co/svalabs/gbert-large-zeroshot-nli) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0518
- F1: 0.9826

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
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| No log        | 0.99  | 36   | 0.5165          | 0.8542 |
| No log        | 1.99  | 72   | 0.1459          | 0.9599 |
| No log        | 2.99  | 108  | 0.0733          | 0.9882 |
| No log        | 3.99  | 144  | 0.1385          | 0.9502 |
| No log        | 4.99  | 180  | 0.0948          | 0.9806 |
| No log        | 5.99  | 216  | 0.0699          | 0.9822 |
| No log        | 6.99  | 252  | 0.0582          | 0.9859 |
| No log        | 7.99  | 288  | 0.0340          | 0.9933 |
| No log        | 8.99  | 324  | 0.0475          | 0.9826 |
| No log        | 9.99  | 360  | 0.0518          | 0.9826 |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1
