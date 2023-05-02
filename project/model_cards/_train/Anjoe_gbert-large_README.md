---
tags:
- generated_from_trainer
model-index:
- name: gbert-large
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gbert-large

This model is a fine-tuned version of deepset/gbert-large 

It was fine-tuned on poetry from Projekt Gutenberg in order to do masked language modeling tasks in poetry generation (synonym creation for rythm and to find rhyming pairs) 

- Loss: 2.1519

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 2.7515        | 1.0   | 2481  | 2.5493          |
| 2.5626        | 2.0   | 4962  | 2.4392          |
| 2.4839        | 3.0   | 7443  | 2.3692          |
| 2.4082        | 4.0   | 9924  | 2.3425          |
| 2.3109        | 5.0   | 12405 | 2.2934          |
| 2.2551        | 6.0   | 14886 | 2.2582          |
| 2.2154        | 7.0   | 17367 | 2.2062          |
| 2.2003        | 8.0   | 19848 | 2.1962          |
| 2.1616        | 9.0   | 22329 | 2.1991          |
| 2.1462        | 10.0  | 24810 | 2.1519          |


### Framework versions

- Transformers 4.19.4
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
