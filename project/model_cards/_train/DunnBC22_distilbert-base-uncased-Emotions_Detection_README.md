---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased-Emotions_Detection
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-Emotions_Detection

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1440
- Accuracy: 0.9345
- F1 Score: 0.9347

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1 Score |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| 0.7287        | 1.0   | 250  | 0.2597          | 0.8955   | 0.8948   |
| 0.2054        | 2.0   | 500  | 0.1638          | 0.9325   | 0.9326   |
| 0.1338        | 3.0   | 750  | 0.1415          | 0.935    | 0.9350   |
| 0.1067        | 4.0   | 1000 | 0.1440          | 0.9345   | 0.9347   |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
