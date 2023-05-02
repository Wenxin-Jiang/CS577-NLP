---
language:
- pt
license: mit
tags:
- generated_from_trainer
model-index:
- name: xlm-roberta-large-finetuned-lener_br
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-large-finetuned-lener_br

This model is a fine-tuned version of [xlm-roberta-large](https://huggingface.co/xlm-roberta-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: nan

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 1.5002        | 1.0   | 8316  | nan             |
| 1.2398        | 2.0   | 16632 | nan             |
| 1.0864        | 3.0   | 24948 | nan             |
| 0.9896        | 4.0   | 33264 | nan             |
| 0.8752        | 5.0   | 41580 | nan             |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
