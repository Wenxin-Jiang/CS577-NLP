---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-16-9
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-16-9

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1121
- Accuracy: 0.16

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
| 1.1038        | 1.0   | 10   | 1.1243          | 0.1      |
| 1.0859        | 2.0   | 20   | 1.1182          | 0.2      |
| 1.0234        | 3.0   | 30   | 1.1442          | 0.3      |
| 0.9493        | 4.0   | 40   | 1.2239          | 0.1      |
| 0.8114        | 5.0   | 50   | 1.2023          | 0.4      |
| 0.6464        | 6.0   | 60   | 1.2329          | 0.4      |
| 0.4731        | 7.0   | 70   | 1.2971          | 0.5      |
| 0.3355        | 8.0   | 80   | 1.3913          | 0.4      |
| 0.1268        | 9.0   | 90   | 1.4670          | 0.5      |
| 0.0747        | 10.0  | 100  | 1.7961          | 0.4      |
| 0.0449        | 11.0  | 110  | 1.8168          | 0.5      |
| 0.0307        | 12.0  | 120  | 1.9307          | 0.4      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
