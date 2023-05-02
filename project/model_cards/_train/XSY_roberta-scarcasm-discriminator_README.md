---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: roberta-scarcasm-discriminator
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-scarcasm-discriminator

roberta-base

label0: unsarcasitic

label1: sarcastic
The fine tune method in my github https://github.com/yangyangxusheng/Fine-tune-use-transformers

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1844
- Accuracy: 0.9698

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
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.144         | 1.0   | 2179 | 0.2522          | 0.9215   |
| 0.116         | 2.0   | 4358 | 0.2105          | 0.9530   |
| 0.0689        | 3.0   | 6537 | 0.2015          | 0.9610   |
| 0.028         | 4.0   | 8716 | 0.1844          | 0.9698   |


### Framework versions

- Transformers 4.12.3
- Pytorch 1.9.0+cu111
- Datasets 1.15.1
- Tokenizers 0.10.3
