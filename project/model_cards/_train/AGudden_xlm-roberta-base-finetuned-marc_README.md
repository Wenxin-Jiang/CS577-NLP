---
license: mit
tags:
- generated_from_trainer
datasets:
- dutch_social
model-index:
- name: xlm-roberta-base-finetuned-marc
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-finetuned-marc

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the dutch_social dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1992
- Mae: 0.0532

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
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Mae    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 0.2824        | 1.0   | 10176 | 0.2370          | 0.0748 |
| 0.1809        | 2.0   | 20352 | 0.1992          | 0.0532 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
