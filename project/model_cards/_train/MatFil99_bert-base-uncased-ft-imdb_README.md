---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-base-uncased-ft-imdb
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-ft-imdb

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the [steciuk/imdb](https://huggingface.co/datasets/steciuk/imdb) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2556
- Accuracy: 0.945
- F1: 0.9441

and flowing results on the testing set:
- Accuracy: 0.9417
- F1: 0.9431

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
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.2943        | 0.38  | 750  | 0.1877          | 0.9257   | 0.9226 |
| 0.2133        | 0.75  | 1500 | 0.1806          | 0.9375   | 0.9347 |
| 0.1811        | 1.12  | 2250 | 0.1783          | 0.9443   | 0.9434 |
| 0.1274        | 1.5   | 3000 | 0.2072          | 0.942    | 0.9400 |
| 0.1177        | 1.88  | 3750 | 0.2737          | 0.9325   | 0.9336 |
| 0.0817        | 2.25  | 4500 | 0.2706          | 0.9435   | 0.9420 |
| 0.0644        | 2.62  | 5250 | 0.2630          | 0.9447   | 0.9434 |
| 0.0604        | 3.0   | 6000 | 0.2556          | 0.945    | 0.9441 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
