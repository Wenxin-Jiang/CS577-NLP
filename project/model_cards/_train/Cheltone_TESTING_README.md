---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- accuracy
- f1
model-index:
- name: TESTING
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# TESTING

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1167
- Precision: 0.9561
- Accuracy: 0.9592
- F1: 0.9592

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:--------:|:------:|
| 0.5903        | 0.4   | 500  | 0.4695          | 0.7342    | 0.7728   | 0.7890 |
| 0.3986        | 0.8   | 1000 | 0.3469          | 0.8144    | 0.8596   | 0.8684 |
| 0.2366        | 1.2   | 1500 | 0.1939          | 0.9313    | 0.9260   | 0.9253 |
| 0.1476        | 1.6   | 2000 | 0.1560          | 0.9207    | 0.9452   | 0.9465 |
| 0.1284        | 2.0   | 2500 | 0.1167          | 0.9561    | 0.9592   | 0.9592 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.1.0
- Tokenizers 0.12.1
