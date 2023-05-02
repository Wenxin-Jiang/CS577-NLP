---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: littledatasets
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# littledatasets

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0001

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 85   | 0.0053          |
| No log        | 2.0   | 170  | 0.0002          |
| No log        | 3.0   | 255  | 0.0001          |
| No log        | 4.0   | 340  | 0.0001          |
| No log        | 5.0   | 425  | 0.0001          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.1
- Datasets 2.5.1
- Tokenizers 0.12.1
