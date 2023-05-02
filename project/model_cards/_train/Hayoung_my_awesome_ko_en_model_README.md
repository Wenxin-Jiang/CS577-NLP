---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: my_awesome_ko_en_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# my_awesome_ko_en_model

This model is a fine-tuned version of [KETI-AIR/ke-t5-small](https://huggingface.co/KETI-AIR/ke-t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: nan
- Bleu: 0.0
- Gen Len: 19.0

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
- train_batch_size: 12
- eval_batch_size: 12
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:----:|:-------:|
| No log        | 1.0   | 67   | nan             | 0.0  | 19.0    |
| No log        | 2.0   | 134  | nan             | 0.0  | 19.0    |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.9.0+cu111
- Datasets 2.7.1
- Tokenizers 0.13.2
