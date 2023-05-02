---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- opus_infopankki
model-index:
- name: t5-opus_infopankki-en-zh
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-opus_infopankki-en-zh

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the opus_infopankki dataset.
It achieves the following results on the evaluation set:
- Loss: 2.8797

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
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 3.2786        | 1.0   | 1496 | 2.8797          |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.1.0
- Tokenizers 0.12.1
