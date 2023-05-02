---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- becasv2
model-index:
- name: distilbert-base-uncased-becasv2-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-becasv2-3

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the becasv2 dataset.
It achieves the following results on the evaluation set:
- Loss: 3.1218

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 10
- eval_batch_size: 10
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 9    | 4.6377          |
| No log        | 2.0   | 18   | 3.8511          |
| No log        | 3.0   | 27   | 3.3758          |
| No log        | 4.0   | 36   | 3.1910          |
| No log        | 5.0   | 45   | 3.1187          |
| No log        | 6.0   | 54   | 3.1009          |
| No log        | 7.0   | 63   | 3.1131          |
| No log        | 8.0   | 72   | 3.1218          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
