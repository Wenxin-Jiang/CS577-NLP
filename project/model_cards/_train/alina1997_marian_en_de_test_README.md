---
language:
- en
- de
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: trained_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# trained_model

This model is a fine-tuned version of [opus-mt-en-de](https://huggingface.co/opus-mt-en-de) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4519
- Bleu: 27.6198
- Gen Len: 106.0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|
| No log        | 1.0   | 3    | 1.4519          | 27.6198 | 106.0   |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.8.0
- Datasets 1.18.3
- Tokenizers 0.10.3
