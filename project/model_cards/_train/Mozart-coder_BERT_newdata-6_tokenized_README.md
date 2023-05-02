---
tags:
- generated_from_trainer
model-index:
- name: BERT_newdata-6_tokenized
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERT_newdata-6_tokenized

This model is a fine-tuned version of [armheb/DNA_bert_6](https://huggingface.co/armheb/DNA_bert_6) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0378

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.0669        | 1.0   | 223  | 0.0373          |
| 0.0394        | 2.0   | 446  | 0.0398          |
| 0.0369        | 3.0   | 669  | 0.0371          |
| 0.0362        | 4.0   | 892  | 0.0358          |
| 0.0383        | 5.0   | 1115 | 0.0353          |
| 0.0365        | 6.0   | 1338 | 0.0378          |
| 0.0366        | 7.0   | 1561 | 0.0377          |
| 0.0373        | 8.0   | 1784 | 0.0359          |
| 0.0372        | 9.0   | 2007 | 0.0371          |
| 0.0377        | 10.0  | 2230 | 0.0357          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
