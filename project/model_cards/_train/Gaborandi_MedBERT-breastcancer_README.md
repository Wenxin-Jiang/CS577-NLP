---
license: mit
tags:
- generated_from_trainer
model-index:
- name: MedBERT-breastcancer
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedBERT-breastcancer

This model is a fine-tuned version of [Charangan/MedBERT](https://huggingface.co/Charangan/MedBERT) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9742

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
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| No log        | 1.0   | 12263 | 1.0881          |
| No log        | 2.0   | 24526 | 1.0259          |
| No log        | 3.0   | 36789 | 0.9937          |
| No log        | 4.0   | 49052 | 0.9831          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.8.0
- Datasets 2.2.2
- Tokenizers 0.13.2
