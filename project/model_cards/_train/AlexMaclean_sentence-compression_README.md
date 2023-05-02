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
- name: sentence-compression
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sentence-compression

This model is a fine-tuned version of [distilbert-base-cased](https://huggingface.co/distilbert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2973
- Accuracy: 0.8912
- F1: 0.8367
- Precision: 0.8495
- Recall: 0.8243

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

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.2686        | 1.0   | 10000 | 0.2667          | 0.8894   | 0.8283 | 0.8725    | 0.7884 |
| 0.2205        | 2.0   | 20000 | 0.2704          | 0.8925   | 0.8372 | 0.8579    | 0.8175 |
| 0.1476        | 3.0   | 30000 | 0.2973          | 0.8912   | 0.8367 | 0.8495    | 0.8243 |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.10.0+cu113
- Datasets 1.16.1
- Tokenizers 0.10.3
