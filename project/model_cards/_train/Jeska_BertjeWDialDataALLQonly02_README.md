---
tags:
- generated_from_trainer
model-index:
- name: BertjeWDialDataALLQonly02
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BertjeWDialDataALLQonly02

This model is a fine-tuned version of [GroNLP/bert-base-dutch-cased](https://huggingface.co/GroNLP/bert-base-dutch-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9043

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 12.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 2.2438        | 1.0   | 871   | 2.1122          |
| 2.1235        | 2.0   | 1742  | 2.0784          |
| 2.0712        | 3.0   | 2613  | 2.0679          |
| 2.0034        | 4.0   | 3484  | 2.0546          |
| 1.9375        | 5.0   | 4355  | 2.0277          |
| 1.8911        | 6.0   | 5226  | 2.0364          |
| 1.8454        | 7.0   | 6097  | 1.9812          |
| 1.808         | 8.0   | 6968  | 2.0175          |
| 1.7716        | 9.0   | 7839  | 2.0286          |
| 1.7519        | 10.0  | 8710  | 1.9653          |
| 1.7358        | 11.0  | 9581  | 1.9817          |
| 1.7084        | 12.0  | 10452 | 1.9633          |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0
- Datasets 1.16.1
- Tokenizers 0.10.3
