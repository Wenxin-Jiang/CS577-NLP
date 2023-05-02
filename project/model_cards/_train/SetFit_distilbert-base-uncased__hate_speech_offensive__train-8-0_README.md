---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-8-0
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-8-0

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1097
- Accuracy: 0.132

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
| 1.1065        | 1.0   | 5    | 1.1287          | 0.0      |
| 1.0592        | 2.0   | 10   | 1.1729          | 0.0      |
| 1.0059        | 3.0   | 15   | 1.1959          | 0.0      |
| 0.9129        | 4.0   | 20   | 1.2410          | 0.0      |
| 0.8231        | 5.0   | 25   | 1.2820          | 0.0      |
| 0.7192        | 6.0   | 30   | 1.3361          | 0.0      |
| 0.6121        | 7.0   | 35   | 1.4176          | 0.0      |
| 0.5055        | 8.0   | 40   | 1.5111          | 0.0      |
| 0.4002        | 9.0   | 45   | 1.5572          | 0.0      |
| 0.3788        | 10.0  | 50   | 1.6733          | 0.0      |
| 0.2755        | 11.0  | 55   | 1.7381          | 0.2      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
