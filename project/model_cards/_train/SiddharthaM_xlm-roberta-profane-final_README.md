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
- name: xlm-roberta-profane-final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-profane-final

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3272
- Accuracy: 0.9087
- Precision: 0.8411
- Recall: 0.8441
- F1: 0.8426

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 1.0   | 296  | 0.2705          | 0.9030   | 0.8368    | 0.8192 | 0.8276 |
| 0.3171        | 2.0   | 592  | 0.2174          | 0.9192   | 0.8847    | 0.8204 | 0.8476 |
| 0.3171        | 3.0   | 888  | 0.2250          | 0.9202   | 0.8658    | 0.8531 | 0.8593 |
| 0.2162        | 4.0   | 1184 | 0.2329          | 0.9106   | 0.8422    | 0.8538 | 0.8478 |
| 0.2162        | 5.0   | 1480 | 0.2260          | 0.9183   | 0.8584    | 0.8584 | 0.8584 |
| 0.1766        | 6.0   | 1776 | 0.2638          | 0.9116   | 0.8409    | 0.8651 | 0.8522 |
| 0.146         | 7.0   | 2072 | 0.3088          | 0.9125   | 0.8494    | 0.8464 | 0.8478 |
| 0.146         | 8.0   | 2368 | 0.2873          | 0.9154   | 0.8568    | 0.8459 | 0.8512 |
| 0.1166        | 9.0   | 2664 | 0.3227          | 0.9144   | 0.8518    | 0.8518 | 0.8518 |
| 0.1166        | 10.0  | 2960 | 0.3272          | 0.9087   | 0.8411    | 0.8441 | 0.8426 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
