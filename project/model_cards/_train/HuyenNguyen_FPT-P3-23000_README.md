---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: FPT-P3-23000
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# FPT-P3-23000

This model is a fine-tuned version of [HuyenNguyen/FPT-P3-15000](https://huggingface.co/HuyenNguyen/FPT-P3-15000) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3727
- Wer: 31.4391

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
- training_steps: 1000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.2922        | 0.4   | 200  | 0.3976          | 31.9574 |
| 0.3445        | 0.8   | 400  | 0.3981          | 21.0180 |
| 0.2742        | 1.2   | 600  | 0.3975          | 31.7631 |
| 0.251         | 1.6   | 800  | 0.3820          | 31.2911 |
| 0.2222        | 2.0   | 1000 | 0.3727          | 31.4391 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
