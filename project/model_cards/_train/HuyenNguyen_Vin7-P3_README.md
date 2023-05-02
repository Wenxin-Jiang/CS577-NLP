---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: Vin7-P3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Vin7-P3

This model is a fine-tuned version of [HuyenNguyen/Vin6-P3](https://huggingface.co/HuyenNguyen/Vin6-P3) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2237
- Wer: 11.6272

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 600
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.247         | 0.51  | 200  | 0.2230          | 12.1483 |
| 0.2463        | 1.03  | 400  | 0.2247          | 11.8044 |
| 0.2187        | 1.54  | 600  | 0.2237          | 11.6272 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2