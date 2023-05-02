---
license: mit
tags:
- generated_from_trainer
model-index:
- name: roberta-base-lm-all
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-lm-all

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7109

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

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 1.2966        | 1.0   | 1194  | 1.0711          |
| 1.0858        | 2.0   | 2388  | 0.9740          |
| 1.0055        | 3.0   | 3582  | 0.9273          |
| 0.9301        | 4.0   | 4776  | 0.8784          |
| 0.9021        | 5.0   | 5970  | 0.8731          |
| 0.8479        | 6.0   | 7164  | 0.8406          |
| 0.8142        | 7.0   | 8358  | 0.8172          |
| 0.7858        | 8.0   | 9552  | 0.8158          |
| 0.7529        | 9.0   | 10746 | 0.7922          |
| 0.7189        | 10.0  | 11940 | 0.7855          |
| 0.7032        | 11.0  | 13134 | 0.7761          |
| 0.6795        | 12.0  | 14328 | 0.7549          |
| 0.6673        | 13.0  | 15522 | 0.7277          |
| 0.6412        | 14.0  | 16716 | 0.7121          |
| 0.6321        | 15.0  | 17910 | 0.7168          |
| 0.6198        | 16.0  | 19104 | 0.7109          |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
