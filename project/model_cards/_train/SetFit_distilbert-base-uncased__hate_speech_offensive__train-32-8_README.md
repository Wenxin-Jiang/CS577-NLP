---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-32-8
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-32-8

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9191
- Accuracy: 0.632

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
| 1.1008        | 1.0   | 19   | 1.0877          | 0.4      |
| 1.0354        | 2.0   | 38   | 1.0593          | 0.35     |
| 0.8765        | 3.0   | 57   | 0.9722          | 0.5      |
| 0.6365        | 4.0   | 76   | 0.9271          | 0.55     |
| 0.3944        | 5.0   | 95   | 0.7852          | 0.5      |
| 0.2219        | 6.0   | 114  | 0.9360          | 0.55     |
| 0.126         | 7.0   | 133  | 1.0610          | 0.55     |
| 0.0389        | 8.0   | 152  | 1.0884          | 0.6      |
| 0.0191        | 9.0   | 171  | 1.3483          | 0.55     |
| 0.0108        | 10.0  | 190  | 1.4226          | 0.55     |
| 0.0082        | 11.0  | 209  | 1.4270          | 0.55     |
| 0.0065        | 12.0  | 228  | 1.5074          | 0.55     |
| 0.0059        | 13.0  | 247  | 1.5577          | 0.55     |
| 0.0044        | 14.0  | 266  | 1.5798          | 0.55     |
| 0.0042        | 15.0  | 285  | 1.6196          | 0.55     |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
