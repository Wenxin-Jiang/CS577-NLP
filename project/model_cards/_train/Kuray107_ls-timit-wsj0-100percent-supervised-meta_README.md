---
tags:
- generated_from_trainer
model-index:
- name: ls-timit-wsj0-100percent-supervised-meta
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ls-timit-wsj0-100percent-supervised-meta

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0531
- Wer: 0.0214

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.1618        | 4.57  | 1000 | 0.0500          | 0.0432 |
| 0.0489        | 9.13  | 2000 | 0.0535          | 0.0291 |
| 0.0306        | 13.7  | 3000 | 0.0478          | 0.0275 |
| 0.0231        | 18.26 | 4000 | 0.0531          | 0.0214 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.2
- Datasets 1.18.2
- Tokenizers 0.10.3
