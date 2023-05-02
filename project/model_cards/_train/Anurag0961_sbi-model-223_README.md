---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: sbi-model-223
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sbi-model-223

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5459
- F1: 0.8781

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.146         | 1.0   | 38   | 0.5014          | 0.8525 |
| 0.0779        | 2.0   | 76   | 0.4644          | 0.8862 |
| 0.0432        | 3.0   | 114  | 0.5182          | 0.8811 |
| 0.0319        | 4.0   | 152  | 0.5121          | 0.8865 |
| 0.0356        | 5.0   | 190  | 0.5107          | 0.8894 |
| 0.024         | 6.0   | 228  | 0.5146          | 0.8867 |
| 0.0288        | 7.0   | 266  | 0.5281          | 0.8781 |
| 0.0277        | 8.0   | 304  | 0.5459          | 0.8781 |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Tokenizers 0.13.1
