---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-16-7
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-16-7

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9011
- Accuracy: 0.578

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
| 1.0968        | 1.0   | 10   | 1.1309          | 0.0      |
| 1.0709        | 2.0   | 20   | 1.1237          | 0.1      |
| 0.9929        | 3.0   | 30   | 1.1254          | 0.1      |
| 0.878         | 4.0   | 40   | 1.1206          | 0.5      |
| 0.7409        | 5.0   | 50   | 1.0831          | 0.1      |
| 0.5663        | 6.0   | 60   | 0.9830          | 0.6      |
| 0.4105        | 7.0   | 70   | 0.9919          | 0.5      |
| 0.2912        | 8.0   | 80   | 1.0472          | 0.6      |
| 0.1013        | 9.0   | 90   | 1.1617          | 0.4      |
| 0.0611        | 10.0  | 100  | 1.2789          | 0.6      |
| 0.039         | 11.0  | 110  | 1.4091          | 0.4      |
| 0.0272        | 12.0  | 120  | 1.4974          | 0.4      |
| 0.0189        | 13.0  | 130  | 1.4845          | 0.5      |
| 0.018         | 14.0  | 140  | 1.4924          | 0.5      |
| 0.0131        | 15.0  | 150  | 1.5206          | 0.6      |
| 0.0116        | 16.0  | 160  | 1.5858          | 0.5      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
