---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-base-finetuned-liputan6-coba-coba
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-base-finetuned-liputan6-coba-coba

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6428
- Rouge1: 0.37
- Rouge2: 0.2512
- Rougel: 0.3302
- Rougelsum: 0.3479

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-06
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:------:|:---------:|
| 10.8402       | 1.0   | 4970  | 0.9818          | 0.2754 | 0.1704 | 0.2475 | 0.2597    |
| 1.2001        | 2.0   | 9940  | 0.6614          | 0.3682 | 0.2521 | 0.3291 | 0.3461    |
| 0.9427        | 3.0   | 14910 | 0.6428          | 0.37   | 0.2512 | 0.3302 | 0.3479    |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.0
- Tokenizers 0.13.2
