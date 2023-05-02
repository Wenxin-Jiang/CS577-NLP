---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- mnli
metrics:
- accuracy
model-index:
- name: '42'
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: MNLI
      type: glue
      args: mnli
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8633723892002038
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 42

This model is a fine-tuned version of [bert-large-uncased](https://huggingface.co/bert-large-uncased) on the MNLI dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8447
- Accuracy: 0.8634

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- distributed_type: not_parallel
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.4274        | 1.0   | 12272 | 0.3892          | 0.8524   |
| 0.2844        | 2.0   | 24544 | 0.4079          | 0.8565   |
| 0.1589        | 3.0   | 36816 | 0.5033          | 0.8527   |
| 0.0877        | 4.0   | 49088 | 0.6624          | 0.8576   |
| 0.0426        | 5.0   | 61360 | 0.8447          | 0.8634   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu113
- Datasets 2.7.1
- Tokenizers 0.11.6
