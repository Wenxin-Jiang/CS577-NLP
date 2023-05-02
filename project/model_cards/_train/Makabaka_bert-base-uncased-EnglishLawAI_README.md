---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: bert-base-uncased-issues-128
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-issues-128

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5503

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 16
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.6214        | 1.0   | 291  | 2.2471          |
| 2.0594        | 2.0   | 582  | 1.9293          |
| 1.8563        | 3.0   | 873  | 1.7961          |
| 1.7442        | 4.0   | 1164 | 1.7518          |
| 1.657         | 5.0   | 1455 | 1.7390          |
| 1.577         | 6.0   | 1746 | 1.7173          |
| 1.5071        | 7.0   | 2037 | 1.6223          |
| 1.4661        | 8.0   | 2328 | 1.5691          |
| 1.4365        | 9.0   | 2619 | 1.6280          |
| 1.3827        | 10.0  | 2910 | 1.4641          |
| 1.3517        | 11.0  | 3201 | 1.6498          |
| 1.3294        | 12.0  | 3492 | 1.3006          |
| 1.2836        | 13.0  | 3783 | 1.6520          |
| 1.2867        | 14.0  | 4074 | 1.6064          |
| 1.2819        | 15.0  | 4365 | 1.4131          |
| 1.2611        | 16.0  | 4656 | 1.5503          |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
