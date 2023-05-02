---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: hasoc19-bert-base-multilingual-cased-HatredStatement-new
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hasoc19-bert-base-multilingual-cased-HatredStatement-new

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6565
- Accuracy: 0.7319
- Precision: 0.7320
- Recall: 0.7319
- F1: 0.7307

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
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 1.0   | 296  | 0.5540          | 0.7110   | 0.7147    | 0.7110 | 0.7067 |
| 0.5551        | 2.0   | 592  | 0.5345          | 0.7224   | 0.7673    | 0.7224 | 0.7038 |
| 0.5551        | 3.0   | 888  | 0.5752          | 0.7272   | 0.7430    | 0.7272 | 0.7183 |
| 0.4252        | 4.0   | 1184 | 0.5697          | 0.7376   | 0.7384    | 0.7376 | 0.7359 |
| 0.4252        | 5.0   | 1480 | 0.6335          | 0.7319   | 0.7388    | 0.7319 | 0.7269 |
| 0.3401        | 6.0   | 1776 | 0.6565          | 0.7319   | 0.7320    | 0.7319 | 0.7307 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
