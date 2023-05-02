---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: bert_base_yc_recipe_30
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert_base_yc_recipe_30

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0000

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 121  | 0.0001          |
| No log        | 2.0   | 242  | 0.0000          |
| No log        | 3.0   | 363  | 0.0000          |
| No log        | 4.0   | 484  | 0.0000          |
| 0.0465        | 5.0   | 605  | 0.0000          |
| 0.0465        | 6.0   | 726  | 0.0000          |
| 0.0465        | 7.0   | 847  | 0.0000          |
| 0.0465        | 8.0   | 968  | 0.0000          |
| 0.0           | 9.0   | 1089 | 0.0000          |
| 0.0           | 10.0  | 1210 | 0.0000          |
| 0.0           | 11.0  | 1331 | 0.0000          |
| 0.0           | 12.0  | 1452 | 0.0000          |
| 0.0           | 13.0  | 1573 | 0.0000          |
| 0.0           | 14.0  | 1694 | 0.0000          |
| 0.0           | 15.0  | 1815 | 0.0000          |
| 0.0           | 16.0  | 1936 | 0.0000          |
| 0.0           | 17.0  | 2057 | 0.0000          |
| 0.0           | 18.0  | 2178 | 0.0000          |
| 0.0           | 19.0  | 2299 | 0.0000          |
| 0.0           | 20.0  | 2420 | 0.0000          |
| 0.0           | 21.0  | 2541 | 0.0000          |
| 0.0           | 22.0  | 2662 | 0.0000          |
| 0.0           | 23.0  | 2783 | 0.0000          |
| 0.0           | 24.0  | 2904 | 0.0000          |
| 0.0           | 25.0  | 3025 | 0.0000          |
| 0.0           | 26.0  | 3146 | 0.0000          |
| 0.0           | 27.0  | 3267 | 0.0000          |
| 0.0           | 28.0  | 3388 | 0.0000          |
| 0.0           | 29.0  | 3509 | 0.0000          |
| 0.0           | 30.0  | 3630 | 0.0000          |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.11.0a0+17540c5
- Datasets 2.4.0
- Tokenizers 0.12.1
