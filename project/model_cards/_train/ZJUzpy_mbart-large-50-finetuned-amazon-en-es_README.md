---
license: mit
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mbart-large-50-finetuned-amazon-en-es
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbart-large-50-finetuned-amazon-en-es

This model is a fine-tuned version of [facebook/mbart-large-50](https://huggingface.co/facebook/mbart-large-50) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.9825
- Rouge1: 0.1511
- Rouge2: 0.0537
- Rougel: 0.1393
- Rougelsum: 0.1404

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
| 2.909         | 1.0   | 838  | 2.8106          | 0.1258 | 0.0571 | 0.1248 | 0.1240    |
| 1.8102        | 2.0   | 1676 | 2.8872          | 0.1382 | 0.0675 | 0.1345 | 0.1353    |
| 1.0773        | 3.0   | 2514 | 3.3501          | 0.1528 | 0.0658 | 0.1504 | 0.1504    |
| 0.5431        | 4.0   | 3352 | 3.9495          | 0.1201 | 0.0561 | 0.1153 | 0.1147    |
| 0.2371        | 5.0   | 4190 | 4.5519          | 0.1559 | 0.0732 | 0.1473 | 0.1464    |
| 0.0934        | 6.0   | 5028 | 4.7016          | 0.1531 | 0.0634 | 0.1467 | 0.1453    |
| 0.0375        | 7.0   | 5866 | 4.9661          | 0.1532 | 0.0562 | 0.1426 | 0.1421    |
| 0.0155        | 8.0   | 6704 | 4.9825          | 0.1511 | 0.0537 | 0.1393 | 0.1404    |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
