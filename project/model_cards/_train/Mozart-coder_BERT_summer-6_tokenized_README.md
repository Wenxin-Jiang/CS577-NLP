---
tags:
- generated_from_trainer
model-index:
- name: BERT_summer-6_tokenized
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERT_summer-6_tokenized

This model is a fine-tuned version of [armheb/DNA_bert_6](https://huggingface.co/armheb/DNA_bert_6) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0351

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
| 0.0702        | 1.0   | 256  | 0.0383          |
| 0.0392        | 2.0   | 512  | 0.0402          |
| 0.0384        | 3.0   | 768  | 0.0370          |
| 0.0377        | 4.0   | 1024 | 0.0361          |
| 0.0372        | 5.0   | 1280 | 0.0392          |
| 0.0372        | 6.0   | 1536 | 0.0373          |
| 0.0375        | 7.0   | 1792 | 0.0351          |
| 0.0371        | 8.0   | 2048 | 0.0364          |
| 0.0369        | 9.0   | 2304 | 0.0354          |
| 0.0359        | 10.0  | 2560 | 0.0371          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
