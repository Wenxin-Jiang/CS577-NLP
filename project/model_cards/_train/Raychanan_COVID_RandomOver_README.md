---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: results
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# results

This model is a fine-tuned version of [hfl/chinese-bert-wwm-ext](https://huggingface.co/hfl/chinese-bert-wwm-ext) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4235
- F1: 0.9546

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 1.1307        | 1.0   | 3268  | 0.9040          | 0.0    |
| 0.8795        | 2.0   | 6536  | 0.5532          | 0.9546 |
| 0.8183        | 3.0   | 9804  | 0.3641          | 0.9546 |
| 1.0074        | 4.0   | 13072 | 0.3998          | 0.9546 |
| 0.7947        | 5.0   | 16340 | 0.4235          | 0.9546 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.1.0
- Tokenizers 0.12.1
