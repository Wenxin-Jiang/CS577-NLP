---
tags:
- generated_from_trainer
model-index:
- name: DistilBERT-POWO_Epiphyte_Scratch
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DistilBERT-POWO_Epiphyte_Scratch

This model is a fine-tuned version of [ViktorDo/DistilBERT-POWO_Scratch](https://huggingface.co/ViktorDo/DistilBERT-POWO_Scratch) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1020

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
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.0725        | 1.0   | 2063 | 0.0894          |
| 0.0588        | 2.0   | 4126 | 0.0986          |
| 0.0533        | 3.0   | 6189 | 0.1020          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
