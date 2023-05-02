---
tags:
- generated_from_trainer
model-index:
- name: BertjeWDialDataALLQonly09
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BertjeWDialDataALLQonly09

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
| 2.2439        | 1.0   | 871   | 2.1102          |
| 2.1235        | 2.0   | 1742  | 2.0785          |
| 2.0709        | 3.0   | 2613  | 2.0689          |
| 2.0033        | 4.0   | 3484  | 2.0565          |
| 1.9386        | 5.0   | 4355  | 2.0290          |
| 1.8909        | 6.0   | 5226  | 2.0366          |
| 1.8449        | 7.0   | 6097  | 1.9809          |
| 1.8078        | 8.0   | 6968  | 2.0177          |
| 1.7709        | 9.0   | 7839  | 2.0289          |
| 1.7516        | 10.0  | 8710  | 1.9645          |
| 1.7354        | 11.0  | 9581  | 1.9810          |
| 1.7073        | 12.0  | 10452 | 1.9631          |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0
- Datasets 1.16.1
- Tokenizers 0.10.3
