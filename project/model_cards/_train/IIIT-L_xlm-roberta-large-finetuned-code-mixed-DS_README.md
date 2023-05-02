---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: xlm-roberta-large-finetuned-code-mixed-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-large-finetuned-code-mixed-DS

This model is a fine-tuned version of [xlm-roberta-large](https://huggingface.co/xlm-roberta-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7328
- Accuracy: 0.7022
- Precision: 0.6437
- Recall: 0.6634
- F1: 0.6483

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 8
- eval_batch_size: 16
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.098         | 0.5   | 248  | 1.0944          | 0.5352   | 0.2355    | 0.3344 | 0.2397 |
| 1.0827        | 1.0   | 496  | 1.0957          | 0.5352   | 0.5789    | 0.3379 | 0.2502 |
| 1.0503        | 1.5   | 744  | 0.9969          | 0.5312   | 0.3621    | 0.4996 | 0.3914 |
| 0.9728        | 2.0   | 992  | 0.8525          | 0.6056   | 0.5096    | 0.5565 | 0.4678 |
| 0.9271        | 2.49  | 1240 | 0.7809          | 0.6378   | 0.6014    | 0.6320 | 0.5963 |
| 0.7977        | 2.99  | 1488 | 0.8290          | 0.5875   | 0.5630    | 0.5918 | 0.5390 |
| 0.752         | 3.49  | 1736 | 0.7684          | 0.7123   | 0.6526    | 0.6610 | 0.6558 |
| 0.6846        | 3.99  | 1984 | 0.7328          | 0.7022   | 0.6437    | 0.6634 | 0.6483 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1
