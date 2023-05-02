---
tags:
- generated_from_trainer
datasets:
- korquad
model-index:
- name: komrc_train
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# komrc_train

This model is a fine-tuned version of [beomi/kcbert-base](https://huggingface.co/beomi/kcbert-base) on the korquad dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6544

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
| 0.8187        | 0.31  | 2000  | 0.7377          |
| 0.6947        | 0.63  | 4000  | 0.6934          |
| 0.6352        | 0.94  | 6000  | 0.6544          |
| 0.3869        | 1.25  | 8000  | 0.7633          |
| 0.3812        | 1.56  | 10000 | 0.7047          |
| 0.3579        | 1.88  | 12000 | 0.7097          |
| 0.2053        | 2.19  | 14000 | 0.8511          |
| 0.2173        | 2.5   | 16000 | 0.8457          |
| 0.2094        | 2.82  | 18000 | 0.8433          |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.4
- Tokenizers 0.10.3
