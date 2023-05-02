---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- emotion
model-index:
- name: bert-base-uncased-issues-128
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-issues-128

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the emotion dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3196

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
| 2.6586        | 1.0   | 500  | 2.4203          |
| 2.4655        | 2.0   | 1000 | 2.3889          |
| 2.3769        | 3.0   | 1500 | 2.3279          |
| 2.3024        | 4.0   | 2000 | 2.3623          |
| 2.2178        | 5.0   | 2500 | 2.4500          |
| 2.1352        | 6.0   | 3000 | 2.3042          |
| 2.0793        | 7.0   | 3500 | 2.3053          |
| 2.0462        | 8.0   | 4000 | 2.2402          |
| 1.9886        | 9.0   | 4500 | 2.3407          |
| 1.9393        | 10.0  | 5000 | 2.2826          |
| 1.904         | 11.0  | 5500 | 2.3401          |
| 1.8742        | 12.0  | 6000 | 2.3276          |
| 1.8441        | 13.0  | 6500 | 2.2815          |
| 1.8082        | 14.0  | 7000 | 2.2739          |
| 1.8058        | 15.0  | 7500 | 2.3225          |
| 1.7951        | 16.0  | 8000 | 2.2933          |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
