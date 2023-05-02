---
license: mit
tags:
- generated_from_trainer
model-index:
- name: Kalbert
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Kalbert

This model is a fine-tuned version of [ai4bharat/indic-bert](https://huggingface.co/ai4bharat/indic-bert) on a kannada news dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5324

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 1.5835        | 1.0   | 3953  | 1.7985          |
| 1.6098        | 2.0   | 7906  | 1.7434          |
| 1.5266        | 3.0   | 11859 | 1.6934          |
| 1.5179        | 4.0   | 15812 | 1.6665          |
| 1.5459        | 5.0   | 19765 | 1.6135          |
| 1.5511        | 6.0   | 23718 | 1.6002          |
| 1.5209        | 7.0   | 27671 | 1.5657          |
| 1.5413        | 8.0   | 31624 | 1.5578          |
| 1.4828        | 9.0   | 35577 | 1.5465          |
| 1.4651        | 10.0  | 39530 | 1.5451          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
