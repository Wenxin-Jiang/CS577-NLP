---
license: mit
tags:
- generated_from_trainer
model-index:
- name: gpt2-medium-new
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-medium-new

This model is a fine-tuned version of [gpt2-medium](https://huggingface.co/gpt2-medium) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9274

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
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 279  | 2.2584          |
| 2.3665        | 2.0   | 558  | 2.1151          |
| 2.3665        | 3.0   | 837  | 2.0273          |
| 2.0194        | 4.0   | 1116 | 1.9705          |
| 2.0194        | 5.0   | 1395 | 1.9376          |
| 1.881         | 6.0   | 1674 | 1.9274          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
