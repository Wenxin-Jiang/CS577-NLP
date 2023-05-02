---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mT5_multilingual_XLSum-finetuned-indosum-coba
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mT5_multilingual_XLSum-finetuned-indosum-coba

This model is a fine-tuned version of [csebuetnlp/mT5_multilingual_XLSum](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2594
- Rouge1: 0.4501
- Rouge2: 0.3695
- Rougel: 0.4194
- Rougelsum: 0.4346

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adafactor
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:------:|:---------:|
| 1.6138        | 1.0   | 7131  | 1.2594          | 0.4501 | 0.3695 | 0.4194 | 0.4346    |
| 1.6162        | 2.0   | 14262 | 1.2594          | 0.4501 | 0.3695 | 0.4194 | 0.4346    |
| 1.6151        | 3.0   | 21393 | 1.2594          | 0.4501 | 0.3695 | 0.4194 | 0.4346    |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
