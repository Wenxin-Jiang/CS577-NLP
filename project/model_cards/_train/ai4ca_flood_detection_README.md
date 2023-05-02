---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: flood_detection
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# flood_detection

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1504
- Accuracy: 0.9625
- F1: 0.9388
- Precision: 0.9718
- Recall: 0.9079

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
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.2372        | 1.0   | 1078 | 0.3109          | 0.9372   | 0.8993 | 0.8933    | 0.9054 |
| 0.1676        | 2.0   | 2156 | 0.2451          | 0.9456   | 0.9116 | 0.9178    | 0.9054 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0
- Datasets 2.7.1
- Tokenizers 0.13.2
