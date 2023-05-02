---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: albert-large-v2-subword-masking-domain-adapted-nbme
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-large-v2-subword-masking-domain-adapted-nbme

This model is a fine-tuned version of [albert-large-v2](https://huggingface.co/albert-large-v2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1807

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
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.7821        | 1.0   | 1790 | 1.3868          |
| 1.2825        | 2.0   | 3580 | 1.2248          |
| 1.1817        | 3.0   | 5370 | 1.1712          |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.1.0
- Tokenizers 0.12.1
