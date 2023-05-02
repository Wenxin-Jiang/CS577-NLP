---
tags:
- generated_from_trainer
datasets:
- universal_dependencies
metrics:
- f1
model-index:
- name: rubert-base-cased-finetuned-panx-de
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: universal_dependencies
      type: universal_dependencies
      config: ru_taiga
      split: train
      args: ru_taiga
    metrics:
    - name: F1
      type: f1
      value: 0.6978625703821133
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# rubert-base-cased-finetuned-panx-de

This model is a fine-tuned version of [DeepPavlov/rubert-base-cased](https://huggingface.co/DeepPavlov/rubert-base-cased) on the universal_dependencies dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3352
- F1: 0.6979

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
- train_batch_size: 24
- eval_batch_size: 24
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 1.3039        | 1.0   | 131  | 1.0720          | 0.5871 |
| 0.7911        | 2.0   | 262  | 0.9581          | 0.6335 |
| 0.5448        | 3.0   | 393  | 0.9162          | 0.6718 |
| 0.3709        | 4.0   | 524  | 0.9722          | 0.6819 |
| 0.2565        | 5.0   | 655  | 1.0484          | 0.6847 |
| 0.1923        | 6.0   | 786  | 1.1410          | 0.6924 |
| 0.145         | 7.0   | 917  | 1.1692          | 0.6995 |
| 0.1104        | 8.0   | 1048 | 1.2592          | 0.6981 |
| 0.086         | 9.0   | 1179 | 1.3307          | 0.6972 |
| 0.0715        | 10.0  | 1310 | 1.3352          | 0.6979 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu117
- Datasets 2.7.1
- Tokenizers 0.13.2
