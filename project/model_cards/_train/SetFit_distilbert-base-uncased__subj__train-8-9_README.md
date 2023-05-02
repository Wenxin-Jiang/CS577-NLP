---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__subj__train-8-9
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__subj__train-8-9

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4865
- Accuracy: 0.778

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.7024        | 1.0   | 3    | 0.6843          | 0.75     |
| 0.67          | 2.0   | 6    | 0.6807          | 0.5      |
| 0.6371        | 3.0   | 9    | 0.6677          | 0.5      |
| 0.585         | 4.0   | 12   | 0.6649          | 0.5      |
| 0.5122        | 5.0   | 15   | 0.6707          | 0.5      |
| 0.4379        | 6.0   | 18   | 0.6660          | 0.5      |
| 0.4035        | 7.0   | 21   | 0.6666          | 0.5      |
| 0.323         | 8.0   | 24   | 0.6672          | 0.5      |
| 0.2841        | 9.0   | 27   | 0.6534          | 0.5      |
| 0.21          | 10.0  | 30   | 0.6456          | 0.5      |
| 0.1735        | 11.0  | 33   | 0.6325          | 0.5      |
| 0.133         | 12.0  | 36   | 0.6214          | 0.5      |
| 0.0986        | 13.0  | 39   | 0.6351          | 0.5      |
| 0.081         | 14.0  | 42   | 0.6495          | 0.5      |
| 0.0638        | 15.0  | 45   | 0.6671          | 0.5      |
| 0.0449        | 16.0  | 48   | 0.7156          | 0.5      |
| 0.0399        | 17.0  | 51   | 0.7608          | 0.5      |
| 0.0314        | 18.0  | 54   | 0.7796          | 0.5      |
| 0.0243        | 19.0  | 57   | 0.7789          | 0.5      |
| 0.0227        | 20.0  | 60   | 0.7684          | 0.5      |
| 0.0221        | 21.0  | 63   | 0.7628          | 0.5      |
| 0.0192        | 22.0  | 66   | 0.7728          | 0.5      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
