---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: sentence-compression-roberta
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sentence-compression-roberta

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3465
- Accuracy: 0.8473
- F1: 0.6835
- Precision: 0.6835
- Recall: 0.6835

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.5312        | 1.0   | 50   | 0.5251          | 0.7591   | 0.0040 | 0.75      | 0.0020 |
| 0.4           | 2.0   | 100  | 0.4003          | 0.8200   | 0.5341 | 0.7113    | 0.4275 |
| 0.3355        | 3.0   | 150  | 0.3465          | 0.8473   | 0.6835 | 0.6835    | 0.6835 |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.10.0+cu113
- Datasets 1.16.1
- Tokenizers 0.10.3
