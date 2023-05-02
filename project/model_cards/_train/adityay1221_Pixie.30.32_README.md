---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: Pixie.30.32
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Pixie.30.32

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1623
- Bleu: 47.6437

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 121
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| No log        | 9.09  | 100  | 1.5563          | 21.3462 |
| No log        | 18.18 | 200  | 1.2493          | 29.2353 |
| No log        | 27.27 | 300  | 1.1670          | 32.5700 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0a0+17540c5
- Datasets 2.1.0
- Tokenizers 0.12.1
