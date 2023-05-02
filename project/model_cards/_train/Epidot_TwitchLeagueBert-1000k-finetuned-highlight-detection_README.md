---
tags:
- generated_from_trainer
metrics:
- precision
- f1
- recall
model-index:
- name: TwitchLeagueBert-1000k-finetuned-highlight-detection
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# TwitchLeagueBert-1000k-finetuned-highlight-detection

This model is a fine-tuned version of [Epidot/TwitchLeagueBert-1000k](https://huggingface.co/Epidot/TwitchLeagueBert-1000k) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1146
- Precision: 0.4420
- F1: 0.3977
- Recall: 0.3614

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | F1     | Recall |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|
| 0.0205        | 1.04  | 20000 | 0.1119          | 0.4665    | 0.4689 | 0.4712 |
| 0.0091        | 2.09  | 40000 | 0.1086          | 0.4803    | 0.4447 | 0.4139 |
| 0.0062        | 3.13  | 60000 | 0.1172          | 0.4382    | 0.4192 | 0.4018 |
| 0.0038        | 4.18  | 80000 | 0.1146          | 0.4420    | 0.3977 | 0.3614 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.7.1
- Datasets 2.0.0
- Tokenizers 0.12.1
