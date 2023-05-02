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
- name: bert-base-uncased_token_itr0_2e-05_all_01_03_2022-04_40_10
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased_token_itr0_2e-05_all_01_03_2022-04_40_10

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2741
- Precision: 0.1936
- Recall: 0.3243
- F1: 0.2424
- Accuracy: 0.8764

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 30   | 0.3235          | 0.1062    | 0.2076 | 0.1405 | 0.8556   |
| No log        | 2.0   | 60   | 0.2713          | 0.1710    | 0.3080 | 0.2199 | 0.8872   |
| No log        | 3.0   | 90   | 0.3246          | 0.2010    | 0.3391 | 0.2524 | 0.8334   |
| No log        | 4.0   | 120  | 0.3008          | 0.2011    | 0.3685 | 0.2602 | 0.8459   |
| No log        | 5.0   | 150  | 0.2714          | 0.1780    | 0.3772 | 0.2418 | 0.8661   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
