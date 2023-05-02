---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- becasv2
model-index:
- name: distilbert-base-uncased-becas-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-becas-4

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the becasv2 dataset.
It achieves the following results on the evaluation set:
- Loss: 3.1357

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
- train_batch_size: 10
- eval_batch_size: 10
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 9    | 4.9618          |
| No log        | 2.0   | 18   | 4.1071          |
| No log        | 3.0   | 27   | 3.5438          |
| No log        | 4.0   | 36   | 3.2115          |
| No log        | 5.0   | 45   | 2.9524          |
| No log        | 6.0   | 54   | 3.0645          |
| No log        | 7.0   | 63   | 2.9351          |
| No log        | 8.0   | 72   | 3.1037          |
| No log        | 9.0   | 81   | 3.1132          |
| No log        | 10.0  | 90   | 3.1357          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
