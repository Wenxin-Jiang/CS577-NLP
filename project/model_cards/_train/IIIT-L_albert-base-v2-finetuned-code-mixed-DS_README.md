---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: albert-base-v2-finetuned-code-mixed-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-base-v2-finetuned-code-mixed-DS

This model is a fine-tuned version of [albert-base-v2](https://huggingface.co/albert-base-v2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0408
- Accuracy: 0.7324
- Precision: 0.6883
- Recall: 0.6822
- F1: 0.6833

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1.2766380106570283e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.9207        | 1.0   | 497  | 0.7810          | 0.6016   | 0.5878    | 0.5953 | 0.5264 |
| 0.7519        | 2.0   | 994  | 0.8159          | 0.6600   | 0.6020    | 0.6194 | 0.6015 |
| 0.6029        | 3.0   | 1491 | 0.8026          | 0.7163   | 0.6599    | 0.6604 | 0.6593 |
| 0.4259        | 4.0   | 1988 | 0.9464          | 0.7384   | 0.7058    | 0.6808 | 0.6822 |
| 0.2845        | 5.0   | 2485 | 1.0408          | 0.7324   | 0.6883    | 0.6822 | 0.6833 |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
