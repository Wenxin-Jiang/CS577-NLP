---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-small-finetuned-amazon-pr-zhsum
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-small-finetuned-amazon-pr-zhsum

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1751
- Rouge1: 0.1109
- Rouge2: 0.0318
- Rougel: 0.1109
- Rougelsum: 0.1115

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| 6.0524        | 1.0   | 381  | 1.5214          | 0.0997 | 0.0281 | 0.0991 | 0.1001    |
| 2.0421        | 2.0   | 762  | 1.4323          | 0.1085 | 0.0287 | 0.1087 | 0.1090    |
| 1.6931        | 3.0   | 1143 | 1.3138          | 0.1118 | 0.0292 | 0.1118 | 0.1123    |
| 1.5288        | 4.0   | 1524 | 1.2603          | 0.1102 | 0.0314 | 0.1101 | 0.1105    |
| 1.4346        | 5.0   | 1905 | 1.2373          | 0.1096 | 0.0297 | 0.1094 | 0.1099    |
| 1.3827        | 6.0   | 2286 | 1.1859          | 0.1101 | 0.0305 | 0.1099 | 0.1105    |
| 1.3167        | 7.0   | 2667 | 1.1778          | 0.1104 | 0.0311 | 0.1104 | 0.1109    |
| 1.3248        | 8.0   | 3048 | 1.1751          | 0.1109 | 0.0318 | 0.1109 | 0.1115    |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.2
