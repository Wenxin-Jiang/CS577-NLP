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
- name: FakevsRealNews
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# FakevsRealNews

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0000
- Accuracy: 1.0
- F1: 1.0
- Precision: 1.0
- Recall: 1.0

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
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1  | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---:|:---------:|:------:|
| 0.0554        | 1.0   | 1956 | 0.0000          | 1.0      | 1.0 | 1.0       | 1.0    |
| 0.0006        | 2.0   | 3912 | 0.0000          | 1.0      | 1.0 | 1.0       | 1.0    |
| 0.0           | 3.0   | 5868 | 0.0000          | 1.0      | 1.0 | 1.0       | 1.0    |


### Framework versions

- Transformers 4.27.2
- Pytorch 1.13.1+cu116
- Datasets 2.10.1
- Tokenizers 0.13.2
