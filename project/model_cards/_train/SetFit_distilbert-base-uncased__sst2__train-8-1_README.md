---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-8-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-8-1

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6930
- Accuracy: 0.5047

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
| 0.7082        | 1.0   | 3    | 0.7048          | 0.25     |
| 0.6761        | 2.0   | 6    | 0.7249          | 0.25     |
| 0.6653        | 3.0   | 9    | 0.7423          | 0.25     |
| 0.6212        | 4.0   | 12   | 0.7727          | 0.25     |
| 0.5932        | 5.0   | 15   | 0.8098          | 0.25     |
| 0.5427        | 6.0   | 18   | 0.8496          | 0.25     |
| 0.5146        | 7.0   | 21   | 0.8992          | 0.25     |
| 0.4356        | 8.0   | 24   | 0.9494          | 0.25     |
| 0.4275        | 9.0   | 27   | 0.9694          | 0.25     |
| 0.3351        | 10.0  | 30   | 0.9968          | 0.25     |
| 0.2812        | 11.0  | 33   | 1.0056          | 0.5      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
