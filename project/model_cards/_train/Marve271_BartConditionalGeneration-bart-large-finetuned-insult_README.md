---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: BartConditionalGeneration-bart-large-finetuned-insult
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BartConditionalGeneration-bart-large-finetuned-insult

This model is a fine-tuned version of [facebook/bart-large](https://huggingface.co/facebook/bart-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.7901

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 5.6217        | 1.0   | 568  | 4.5864          |
| 4.7444        | 2.0   | 1136 | nan             |
| 4.2308        | 3.0   | 1704 | 3.7590          |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
