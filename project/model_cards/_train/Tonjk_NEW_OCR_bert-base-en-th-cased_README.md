---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: NEW_OCR_bert-base-en-th-cased
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# NEW_OCR_bert-base-en-th-cased

This model is a fine-tuned version of [Geotrend/bert-base-en-th-cased](https://huggingface.co/Geotrend/bert-base-en-th-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0103

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
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.0519        | 1.0   | 5351  | 0.0141          |
| 0.0131        | 2.0   | 10702 | 0.0116          |
| 0.0105        | 3.0   | 16053 | 0.0105          |
| 0.0087        | 4.0   | 21404 | 0.0102          |
| 0.0074        | 5.0   | 26755 | 0.0103          |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.12.1+cu113
- Datasets 1.17.0
- Tokenizers 0.10.3
