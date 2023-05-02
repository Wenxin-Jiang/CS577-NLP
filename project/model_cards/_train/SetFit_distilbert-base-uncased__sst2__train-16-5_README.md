---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-16-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-16-5

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6537
- Accuracy: 0.6332

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
| 0.6925        | 1.0   | 7    | 0.6966          | 0.2857   |
| 0.6703        | 2.0   | 14   | 0.7045          | 0.2857   |
| 0.6404        | 3.0   | 21   | 0.7205          | 0.2857   |
| 0.555         | 4.0   | 28   | 0.7548          | 0.2857   |
| 0.5179        | 5.0   | 35   | 0.6745          | 0.5714   |
| 0.3038        | 6.0   | 42   | 0.7260          | 0.5714   |
| 0.2089        | 7.0   | 49   | 0.8016          | 0.5714   |
| 0.1303        | 8.0   | 56   | 0.8202          | 0.5714   |
| 0.0899        | 9.0   | 63   | 0.9966          | 0.5714   |
| 0.0552        | 10.0  | 70   | 1.1887          | 0.5714   |
| 0.0333        | 11.0  | 77   | 1.2163          | 0.5714   |
| 0.0169        | 12.0  | 84   | 1.2874          | 0.5714   |
| 0.0136        | 13.0  | 91   | 1.3598          | 0.5714   |
| 0.0103        | 14.0  | 98   | 1.4237          | 0.5714   |
| 0.0089        | 15.0  | 105  | 1.4758          | 0.5714   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
