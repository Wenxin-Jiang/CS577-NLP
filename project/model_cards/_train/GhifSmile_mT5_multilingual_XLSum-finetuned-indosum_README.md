---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mT5_multilingual_XLSum-finetuned-indosum
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mT5_multilingual_XLSum-finetuned-indosum

This model is a fine-tuned version of [csebuetnlp/mT5_multilingual_XLSum](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5512
- Rouge1: 0.3819
- Rouge2: 0.3102
- Rougel: 0.3529
- Rougelsum: 0.3687

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
| 1.8183        | 1.0   | 7131  | 1.5512          | 0.3819 | 0.3102 | 0.3529 | 0.3687    |
| 1.8191        | 2.0   | 14262 | 1.5512          | 0.3819 | 0.3102 | 0.3529 | 0.3687    |
| 1.8197        | 3.0   | 21393 | 1.5512          | 0.3819 | 0.3102 | 0.3529 | 0.3687    |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
