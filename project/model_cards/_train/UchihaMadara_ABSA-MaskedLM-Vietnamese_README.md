---
tags:
- generated_from_trainer
datasets:
- vietnamese_students_feedback
model-index:
- name: ABSA-MaskedLM-Vietnamese
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ABSA-MaskedLM-Vietnamese

This model is a fine-tuned version of [vinai/phobert-base](https://huggingface.co/vinai/phobert-base) on the vietnamese_students_feedback dataset.
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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.077         | 1.0   | 220  | 0.0398          |
| 0.0415        | 2.0   | 440  | 0.0370          |
| 0.0381        | 3.0   | 660  | 0.0351          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
