---
tags:
- generated_from_trainer
model-index:
- name: neg_komrc_train
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# neg_komrc_train

This model is a fine-tuned version of [beomi/kcbert-base](https://huggingface.co/beomi/kcbert-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4016

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
- seed: 1234
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.277         | 0.51  | 10000 | 0.4016          |
| 0.1671        | 1.03  | 20000 | 0.4116          |
| 0.1725        | 1.54  | 30000 | 0.4390          |
| 0.0868        | 2.06  | 40000 | 0.5147          |
| 0.0868        | 2.57  | 50000 | 0.5064          |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.4
- Tokenizers 0.10.3
