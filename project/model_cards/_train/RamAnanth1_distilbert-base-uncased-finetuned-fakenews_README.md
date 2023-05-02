---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-base-uncased-finetuned-fakenews
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-fakenews

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0656
- Accuracy: 0.9901
- F1: 0.9909

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|
| 0.0505        | 1.0   | 3045  | 0.2405          | 0.9651   | 0.9685 |
| 0.0463        | 2.0   | 6090  | 0.0473          | 0.9872   | 0.9881 |
| 0.0272        | 3.0   | 9135  | 0.0607          | 0.9892   | 0.9900 |
| 0.0154        | 4.0   | 12180 | 0.0522          | 0.9892   | 0.9900 |
| 0.0047        | 5.0   | 15225 | 0.0717          | 0.9895   | 0.9903 |
| 0.0024        | 6.0   | 18270 | 0.0656          | 0.9901   | 0.9909 |


### Framework versions

- Transformers 4.22.0
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
