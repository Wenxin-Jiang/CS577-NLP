---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: ELL_pretrained
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ELL_pretrained

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9006

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
| 2.1542        | 1.0   | 1627 | 2.1101          |
| 2.0739        | 2.0   | 3254 | 2.0006          |
| 2.0241        | 3.0   | 4881 | 1.7874          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
