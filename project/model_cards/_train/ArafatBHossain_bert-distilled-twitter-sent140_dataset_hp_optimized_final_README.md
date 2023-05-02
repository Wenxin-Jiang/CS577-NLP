---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-distilled-twitter-sent140_dataset_hp_optimized_final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-distilled-twitter-sent140_dataset_hp_optimized_final

This model is a fine-tuned version of [ArafatBHossain/distilbert-base-uncased_fine_tuned_sent140](https://huggingface.co/ArafatBHossain/distilbert-base-uncased_fine_tuned_sent140) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7526
- Accuracy: 0.7701

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1.0252171333853176e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.5666        | 1.0   | 408  | 0.7110          | 0.7647   |
| 0.501         | 2.0   | 816  | 0.7382          | 0.7567   |
| 0.5199        | 3.0   | 1224 | 0.7562          | 0.7674   |
| 0.4972        | 4.0   | 1632 | 0.7502          | 0.7647   |
| 0.4498        | 5.0   | 2040 | 0.7526          | 0.7701   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.11.0
- Datasets 2.7.1
- Tokenizers 0.12.1
