---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-8-8
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-8-8

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6925
- Accuracy: 0.5200

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
| 0.7061        | 1.0   | 3    | 0.6899          | 0.75     |
| 0.6627        | 2.0   | 6    | 0.7026          | 0.25     |
| 0.644         | 3.0   | 9    | 0.7158          | 0.25     |
| 0.6087        | 4.0   | 12   | 0.7325          | 0.25     |
| 0.5602        | 5.0   | 15   | 0.7555          | 0.25     |
| 0.5034        | 6.0   | 18   | 0.7725          | 0.25     |
| 0.4672        | 7.0   | 21   | 0.7983          | 0.25     |
| 0.403         | 8.0   | 24   | 0.8314          | 0.25     |
| 0.3571        | 9.0   | 27   | 0.8555          | 0.25     |
| 0.2792        | 10.0  | 30   | 0.9065          | 0.25     |
| 0.2373        | 11.0  | 33   | 0.9286          | 0.25     |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
