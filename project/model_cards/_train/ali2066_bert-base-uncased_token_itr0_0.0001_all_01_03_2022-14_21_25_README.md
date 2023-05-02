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
- name: bert-base-uncased_token_itr0_0.0001_all_01_03_2022-14_21_25
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased_token_itr0_0.0001_all_01_03_2022-14_21_25

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2698
- Precision: 0.3321
- Recall: 0.5265
- F1: 0.4073
- Accuracy: 0.8942

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 30   | 0.3314          | 0.1627    | 0.3746 | 0.2269 | 0.8419   |
| No log        | 2.0   | 60   | 0.2957          | 0.2887    | 0.4841 | 0.3617 | 0.8592   |
| No log        | 3.0   | 90   | 0.2905          | 0.2429    | 0.5141 | 0.3299 | 0.8651   |
| No log        | 4.0   | 120  | 0.2759          | 0.3137    | 0.5565 | 0.4013 | 0.8787   |
| No log        | 5.0   | 150  | 0.2977          | 0.3116    | 0.5565 | 0.3995 | 0.8796   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
