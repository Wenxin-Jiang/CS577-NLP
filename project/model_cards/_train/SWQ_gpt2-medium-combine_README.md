---
license: mit
tags:
- generated_from_trainer
model-index:
- name: gpt2-medium-combine
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-medium-combine

This model is a fine-tuned version of [gpt2-medium](https://huggingface.co/gpt2-medium) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.7295

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 8e-06
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.9811        | 0.6   | 500  | 2.8135          |
| 2.8017        | 1.2   | 1000 | 2.7691          |
| 2.7255        | 1.81  | 1500 | 2.7480          |
| 2.6598        | 2.41  | 2000 | 2.7392          |
| 2.6426        | 3.01  | 2500 | 2.7306          |
| 2.6138        | 3.61  | 3000 | 2.7295          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
