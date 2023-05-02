---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-8-8
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-8-8

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0005
- Accuracy: 0.518

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
| 1.1029        | 1.0   | 5    | 1.1295          | 0.0      |
| 1.0472        | 2.0   | 10   | 1.1531          | 0.0      |
| 1.054         | 3.0   | 15   | 1.1475          | 0.0      |
| 0.9366        | 4.0   | 20   | 1.1515          | 0.0      |
| 0.8698        | 5.0   | 25   | 1.1236          | 0.4      |
| 0.8148        | 6.0   | 30   | 1.0716          | 0.6      |
| 0.6884        | 7.0   | 35   | 1.0662          | 0.6      |
| 0.5641        | 8.0   | 40   | 1.0671          | 0.6      |
| 0.5           | 9.0   | 45   | 1.0282          | 0.6      |
| 0.3882        | 10.0  | 50   | 1.0500          | 0.6      |
| 0.3522        | 11.0  | 55   | 1.1381          | 0.6      |
| 0.2492        | 12.0  | 60   | 1.1278          | 0.6      |
| 0.2063        | 13.0  | 65   | 1.0731          | 0.6      |
| 0.1608        | 14.0  | 70   | 1.1339          | 0.6      |
| 0.1448        | 15.0  | 75   | 1.1892          | 0.6      |
| 0.0925        | 16.0  | 80   | 1.1840          | 0.6      |
| 0.0768        | 17.0  | 85   | 1.0608          | 0.6      |
| 0.0585        | 18.0  | 90   | 1.1073          | 0.6      |
| 0.0592        | 19.0  | 95   | 1.3134          | 0.6      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
