---
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: Vin14-P3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Vin14-P3

This model is a fine-tuned version of [HuyenNguyen/Vin12-P3](https://huggingface.co/HuyenNguyen/Vin12-P3) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3766
- Wer: 24.0523

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
- training_steps: 400
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.1675        | 0.57  | 100  | 0.3491          | 23.3601 |
| 0.0998        | 1.15  | 200  | 0.3407          | 22.3272 |
| 0.0872        | 1.72  | 300  | 0.3603          | 23.7776 |
| 0.0323        | 2.3   | 400  | 0.3766          | 24.0523 |


### Framework versions

- Transformers 4.27.0.dev0
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
