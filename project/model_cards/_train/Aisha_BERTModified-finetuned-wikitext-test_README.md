---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: BERTModified-finetuned-wikitext-test
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERTModified-finetuned-wikitext-test

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 6.7191

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 9.5075        | 1.0   | 63   | 8.9689          |
| 8.5623        | 2.0   | 126  | 8.1532          |
| 7.8617        | 3.0   | 189  | 7.6296          |
| 7.4107        | 4.0   | 252  | 7.3166          |
| 7.0526        | 5.0   | 315  | 6.9171          |
| 6.8774        | 6.0   | 378  | 6.8958          |
| 6.8026        | 7.0   | 441  | 6.7981          |
| 6.6463        | 8.0   | 504  | 6.7992          |
| 6.6569        | 9.0   | 567  | 6.7409          |
| 6.5931        | 10.0  | 630  | 6.6189          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.13.0+cu117
- Datasets 2.6.1
- Tokenizers 0.13.1
