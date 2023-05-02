---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-small-finetuned-amazon-en-es-Resumen-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-small-finetuned-amazon-en-es-Resumen-2

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.0910
- Rouge1: 16.3799
- Rouge2: 7.6088
- Rougel: 15.9886
- Rougelsum: 16.1691

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|
| 7.004         | 1.0   | 1209 | 3.3408          | 13.3874 | 5.2828 | 12.9812 | 12.9666   |
| 3.9036        | 2.0   | 2418 | 3.2286          | 15.9158 | 7.7591 | 15.2863 | 15.3932   |
| 3.598         | 3.0   | 3627 | 3.1778          | 16.0628 | 7.1178 | 15.1227 | 15.2487   |
| 3.4228        | 4.0   | 4836 | 3.1147          | 15.9998 | 7.6239 | 15.3691 | 15.4711   |
| 3.3212        | 5.0   | 6045 | 3.1049          | 16.5369 | 7.743  | 16.2272 | 16.3427   |
| 3.2658        | 6.0   | 7254 | 3.0974          | 17.4125 | 8.0961 | 17.0223 | 17.136    |
| 3.2105        | 7.0   | 8463 | 3.0911          | 16.5786 | 7.7369 | 16.1889 | 16.3189   |
| 3.184         | 8.0   | 9672 | 3.0910          | 16.3799 | 7.6088 | 15.9886 | 16.1691   |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
