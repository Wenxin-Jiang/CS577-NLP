---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-16-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-16-5

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9907
- Accuracy: 0.49

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
| 1.0941        | 1.0   | 10   | 1.1287          | 0.2      |
| 1.0481        | 2.0   | 20   | 1.1136          | 0.2      |
| 0.9498        | 3.0   | 30   | 1.1200          | 0.2      |
| 0.8157        | 4.0   | 40   | 1.0771          | 0.2      |
| 0.65          | 5.0   | 50   | 0.9733          | 0.4      |
| 0.5021        | 6.0   | 60   | 1.0626          | 0.4      |
| 0.3358        | 7.0   | 70   | 1.0787          | 0.4      |
| 0.2017        | 8.0   | 80   | 1.3183          | 0.4      |
| 0.088         | 9.0   | 90   | 1.2204          | 0.5      |
| 0.0527        | 10.0  | 100  | 1.6892          | 0.4      |
| 0.0337        | 11.0  | 110  | 1.6967          | 0.5      |
| 0.0238        | 12.0  | 120  | 1.5436          | 0.5      |
| 0.0183        | 13.0  | 130  | 1.7447          | 0.4      |
| 0.0159        | 14.0  | 140  | 1.8999          | 0.4      |
| 0.014         | 15.0  | 150  | 1.9004          | 0.4      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
