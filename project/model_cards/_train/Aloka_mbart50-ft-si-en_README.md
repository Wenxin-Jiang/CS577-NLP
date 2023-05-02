---
tags:
- generated_from_trainer
model_index:
- name: mbart50-ft-si-en
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbart50-ft-si-en

This model was trained from scratch on an unkown dataset.
It achieves the following results on the evaluation set:
- Loss: 5.0476

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0005
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 0.98  | 30   | 5.6367          |
| No log        | 1.98  | 60   | 4.1221          |
| No log        | 2.98  | 90   | 3.1880          |
| No log        | 3.98  | 120  | 3.1175          |
| No log        | 4.98  | 150  | 3.3575          |
| No log        | 5.98  | 180  | 3.7855          |
| No log        | 6.98  | 210  | 4.3530          |
| No log        | 7.98  | 240  | 4.7216          |
| No log        | 8.98  | 270  | 4.9202          |
| No log        | 9.98  | 300  | 5.0476          |


### Framework versions

- Transformers 4.9.2
- Pytorch 1.6.0
- Datasets 1.11.0
- Tokenizers 0.10.3
