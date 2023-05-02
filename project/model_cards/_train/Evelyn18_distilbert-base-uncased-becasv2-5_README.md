---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- becasv2
model-index:
- name: distilbert-base-uncased-becasv2-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-becasv2-5

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the becasv2 dataset.
It achieves the following results on the evaluation set:
- Loss: 3.0409

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
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 6    | 5.3475          |
| No log        | 2.0   | 12   | 4.6045          |
| No log        | 3.0   | 18   | 4.1832          |
| No log        | 4.0   | 24   | 3.8223          |
| No log        | 5.0   | 30   | 3.4798          |
| No log        | 6.0   | 36   | 3.2615          |
| No log        | 7.0   | 42   | 3.1414          |
| No log        | 8.0   | 48   | 3.1067          |
| No log        | 9.0   | 54   | 2.9950          |
| No log        | 10.0  | 60   | 2.9482          |
| No log        | 11.0  | 66   | 2.9536          |
| No log        | 12.0  | 72   | 3.0180          |
| No log        | 13.0  | 78   | 3.0515          |
| No log        | 14.0  | 84   | 3.0444          |
| No log        | 15.0  | 90   | 3.0409          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
