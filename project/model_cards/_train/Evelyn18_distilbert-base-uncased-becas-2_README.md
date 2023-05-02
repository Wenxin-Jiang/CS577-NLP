---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- becasv2
model-index:
- name: distilbert-base-uncased-becas-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-becas-2

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the becasv2 dataset.
It achieves the following results on the evaluation set:
- Loss: 5.9506

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.1
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 5    | 5.9506          |
| No log        | 2.0   | 10   | 5.9506          |
| No log        | 3.0   | 15   | 5.9506          |
| No log        | 4.0   | 20   | 5.9506          |
| No log        | 5.0   | 25   | 5.9506          |
| No log        | 6.0   | 30   | 5.9506          |
| No log        | 7.0   | 35   | 5.9506          |
| No log        | 8.0   | 40   | 5.9506          |
| No log        | 9.0   | 45   | 5.9506          |
| No log        | 10.0  | 50   | 5.9506          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
