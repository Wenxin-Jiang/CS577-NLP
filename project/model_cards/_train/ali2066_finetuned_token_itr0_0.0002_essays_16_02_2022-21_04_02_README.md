---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: finetuned_token_itr0_0.0002_essays_16_02_2022-21_04_02
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_itr0_0.0002_essays_16_02_2022-21_04_02

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2158
- Precision: 0.5814
- Recall: 0.7073
- F1: 0.6382
- Accuracy: 0.9248

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 11   | 0.3920          | 0.4392    | 0.6069 | 0.5096 | 0.8593   |
| No log        | 2.0   | 22   | 0.3304          | 0.4282    | 0.6260 | 0.5085 | 0.8672   |
| No log        | 3.0   | 33   | 0.3361          | 0.4840    | 0.6336 | 0.5488 | 0.8685   |
| No log        | 4.0   | 44   | 0.3258          | 0.5163    | 0.6641 | 0.5810 | 0.8722   |
| No log        | 5.0   | 55   | 0.3472          | 0.5192    | 0.6718 | 0.5857 | 0.8743   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
