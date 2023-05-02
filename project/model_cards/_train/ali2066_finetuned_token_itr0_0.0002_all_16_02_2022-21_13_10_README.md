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
- name: finetuned_token_itr0_0.0002_all_16_02_2022-21_13_10
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_itr0_0.0002_all_16_02_2022-21_13_10

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3057
- Precision: 0.2857
- Recall: 0.4508
- F1: 0.3497
- Accuracy: 0.8741

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
| No log        | 1.0   | 30   | 0.3018          | 0.2097    | 0.2546 | 0.2300 | 0.8727   |
| No log        | 2.0   | 60   | 0.2337          | 0.3444    | 0.3652 | 0.3545 | 0.9024   |
| No log        | 3.0   | 90   | 0.2198          | 0.3463    | 0.3869 | 0.3655 | 0.9070   |
| No log        | 4.0   | 120  | 0.2112          | 0.3757    | 0.4405 | 0.4056 | 0.9173   |
| No log        | 5.0   | 150  | 0.2131          | 0.4163    | 0.5126 | 0.4595 | 0.9212   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
