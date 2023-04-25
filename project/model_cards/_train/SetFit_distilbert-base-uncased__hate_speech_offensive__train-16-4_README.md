---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-16-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-16-4

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0903
- Accuracy: 0.4805

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
| 1.0974        | 1.0   | 10   | 1.1139          | 0.1      |
| 1.0637        | 2.0   | 20   | 1.0988          | 0.1      |
| 0.9758        | 3.0   | 30   | 1.1013          | 0.1      |
| 0.9012        | 4.0   | 40   | 1.0769          | 0.3      |
| 0.6993        | 5.0   | 50   | 1.0484          | 0.6      |
| 0.5676        | 6.0   | 60   | 1.0223          | 0.6      |
| 0.4069        | 7.0   | 70   | 0.9190          | 0.6      |
| 0.3192        | 8.0   | 80   | 1.1370          | 0.6      |
| 0.1112        | 9.0   | 90   | 1.1728          | 0.6      |
| 0.07          | 10.0  | 100  | 1.1998          | 0.6      |
| 0.0397        | 11.0  | 110  | 1.3700          | 0.6      |
| 0.027         | 12.0  | 120  | 1.3329          | 0.6      |
| 0.021         | 13.0  | 130  | 1.2697          | 0.6      |
| 0.0177        | 14.0  | 140  | 1.4195          | 0.6      |
| 0.0142        | 15.0  | 150  | 1.5342          | 0.6      |
| 0.0118        | 16.0  | 160  | 1.5999          | 0.6      |
| 0.0108        | 17.0  | 170  | 1.6327          | 0.6      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
