---
tags:
- generated_from_trainer
model-index:
- name: BERT_autumn-6_tokenized
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERT_autumn-6_tokenized

This model is a fine-tuned version of [armheb/DNA_bert_6](https://huggingface.co/armheb/DNA_bert_6) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0385

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
| 0.0828        | 1.0   | 125  | 0.0406          |
| 0.0395        | 2.0   | 250  | 0.0390          |
| 0.0398        | 3.0   | 375  | 0.0393          |
| 0.0385        | 4.0   | 500  | 0.0381          |
| 0.0384        | 5.0   | 625  | 0.0379          |
| 0.0372        | 6.0   | 750  | 0.0349          |
| 0.0392        | 7.0   | 875  | 0.0358          |
| 0.0381        | 8.0   | 1000 | 0.0391          |
| 0.0372        | 9.0   | 1125 | 0.0379          |
| 0.0365        | 10.0  | 1250 | 0.0354          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
