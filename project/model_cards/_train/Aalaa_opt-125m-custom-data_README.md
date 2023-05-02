---
license: other
tags:
- generated_from_trainer
model-index:
- name: opt-125m-custom-data
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# opt-125m-custom-data

This model is a fine-tuned version of [facebook/opt-125m](https://huggingface.co/facebook/opt-125m) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.9594

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 480  | 2.9889          |
| 3.1368        | 2.0   | 960  | 2.9625          |
| 2.8629        | 3.0   | 1440 | 2.9594          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
