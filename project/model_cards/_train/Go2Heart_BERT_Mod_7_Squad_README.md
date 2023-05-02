---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- squad_v2
model-index:
- name: BERT_Mod_7_Squad
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERT_Mod_7_Squad

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the squad_v2 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0928

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 1.189         | 1.0   | 4089  | 1.2196          |
| 1.0312        | 2.0   | 8178  | 1.0691          |
| 0.8954        | 3.0   | 12267 | 1.0928          |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1
- Datasets 1.17.0
- Tokenizers 0.12.1
