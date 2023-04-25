---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-32-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-32-3

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8286
- Accuracy: 0.661

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
| 1.1041        | 1.0   | 19   | 1.0658          | 0.5      |
| 1.009         | 2.0   | 38   | 0.9892          | 0.7      |
| 0.7925        | 3.0   | 57   | 0.8516          | 0.7      |
| 0.5279        | 4.0   | 76   | 0.7877          | 0.65     |
| 0.2932        | 5.0   | 95   | 0.7592          | 0.65     |
| 0.1166        | 6.0   | 114  | 0.9437          | 0.65     |
| 0.044         | 7.0   | 133  | 1.0315          | 0.75     |
| 0.0197        | 8.0   | 152  | 1.3513          | 0.55     |
| 0.0126        | 9.0   | 171  | 1.1702          | 0.7      |
| 0.0083        | 10.0  | 190  | 1.2272          | 0.7      |
| 0.0068        | 11.0  | 209  | 1.2889          | 0.7      |
| 0.0059        | 12.0  | 228  | 1.3073          | 0.7      |
| 0.0052        | 13.0  | 247  | 1.3595          | 0.7      |
| 0.0041        | 14.0  | 266  | 1.4443          | 0.7      |
| 0.0038        | 15.0  | 285  | 1.4709          | 0.7      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
