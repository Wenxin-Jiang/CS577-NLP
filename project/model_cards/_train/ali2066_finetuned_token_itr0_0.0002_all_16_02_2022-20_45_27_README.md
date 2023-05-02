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
- name: finetuned_token_itr0_0.0002_all_16_02_2022-20_45_27
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_itr0_0.0002_all_16_02_2022-20_45_27

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1500
- Precision: 0.4739
- Recall: 0.5250
- F1: 0.4981
- Accuracy: 0.9551

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
| No log        | 1.0   | 38   | 0.3183          | 0.2024    | 0.2909 | 0.2387 | 0.8499   |
| No log        | 2.0   | 76   | 0.3092          | 0.2909    | 0.4181 | 0.3431 | 0.8548   |
| No log        | 3.0   | 114  | 0.2928          | 0.2923    | 0.4855 | 0.3650 | 0.8647   |
| No log        | 4.0   | 152  | 0.3098          | 0.2832    | 0.4605 | 0.3507 | 0.8641   |
| No log        | 5.0   | 190  | 0.3120          | 0.2470    | 0.4374 | 0.3157 | 0.8654   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
