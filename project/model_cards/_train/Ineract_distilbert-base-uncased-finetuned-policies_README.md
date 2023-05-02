---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- policies
model-index:
- name: distilbert-base-uncased-finetuned-policies
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-policies

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the policies dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0193

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.4208        | 1.0   | 759  | 0.0183          |
| 0.0115        | 2.0   | 1518 | 0.0202          |
| 0.0048        | 3.0   | 2277 | 0.0193          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1
- Datasets 2.8.0
- Tokenizers 0.13.2
