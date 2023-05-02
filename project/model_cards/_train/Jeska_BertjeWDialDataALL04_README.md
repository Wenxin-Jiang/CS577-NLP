---
tags:
- generated_from_trainer
model-index:
- name: BertjeWDialDataALL04
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BertjeWDialDataALL04

This model is a fine-tuned version of [GroNLP/bert-base-dutch-cased](https://huggingface.co/GroNLP/bert-base-dutch-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9717

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
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 2.2954        | 1.0   | 1542  | 2.0372          |
| 2.2015        | 2.0   | 3084  | 2.0104          |
| 2.1661        | 3.0   | 4626  | 2.0372          |
| 2.1186        | 4.0   | 6168  | 1.9549          |
| 2.0939        | 5.0   | 7710  | 1.9438          |
| 2.0867        | 6.0   | 9252  | 1.9648          |
| 2.0462        | 7.0   | 10794 | 1.9465          |
| 2.0315        | 8.0   | 12336 | 1.9412          |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0
- Datasets 1.16.1
- Tokenizers 0.10.3
