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
- Loss: 1.2503

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

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.0976        | 1.0   | 291  | 1.7064          |
| 1.6388        | 2.0   | 582  | 1.4335          |
| 1.4846        | 3.0   | 873  | 1.3750          |
| 1.4003        | 4.0   | 1164 | 1.3749          |
| 1.3393        | 5.0   | 1455 | 1.1970          |
| 1.2848        | 6.0   | 1746 | 1.2826          |
| 1.2385        | 7.0   | 2037 | 1.2652          |
| 1.1974        | 8.0   | 2328 | 1.2158          |
| 1.1653        | 9.0   | 2619 | 1.1808          |
| 1.142         | 10.0  | 2910 | 1.2091          |
| 1.13          | 11.0  | 3201 | 1.2147          |
| 1.1051        | 12.0  | 3492 | 1.1668          |
| 1.0802        | 13.0  | 3783 | 1.2550          |
| 1.0781        | 14.0  | 4074 | 1.1659          |
| 1.0644        | 15.0  | 4365 | 1.1272          |
| 1.0618        | 16.0  | 4656 | 1.2503          |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
