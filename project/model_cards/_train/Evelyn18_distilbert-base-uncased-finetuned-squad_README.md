---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- becasv2
model-index:
- name: distilbert-base-uncased-finetuned-squad
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-squad

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the becasv2 dataset.
It achieves the following results on the evaluation set:
- Loss: 4.0087

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
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 5    | 5.5219          |
| No log        | 2.0   | 10   | 4.9747          |
| No log        | 3.0   | 15   | 4.5448          |
| No log        | 4.0   | 20   | 4.1843          |
| No log        | 5.0   | 25   | 3.8491          |
| No log        | 6.0   | 30   | 3.6789          |
| No log        | 7.0   | 35   | 3.5018          |
| No log        | 8.0   | 40   | 3.4254          |
| No log        | 9.0   | 45   | 3.4566          |
| No log        | 10.0  | 50   | 3.4326          |
| No log        | 11.0  | 55   | 3.5741          |
| No log        | 12.0  | 60   | 3.5260          |
| No log        | 13.0  | 65   | 3.7003          |
| No log        | 14.0  | 70   | 3.7499          |
| No log        | 15.0  | 75   | 3.7961          |
| No log        | 16.0  | 80   | 3.8578          |
| No log        | 17.0  | 85   | 3.9928          |
| No log        | 18.0  | 90   | 4.0305          |
| No log        | 19.0  | 95   | 4.0024          |
| No log        | 20.0  | 100  | 4.0087          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
