---
tags:
- generated_from_trainer
model-index:
- name: bert-base-uncased-pretrained-mlm-coqa-stories
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-pretrained-mlm-coqa-stories

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8310

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.0573        | 1.0   | 2479 | 1.8805          |
| 1.9517        | 2.0   | 4958 | 1.8377          |
| 1.9048        | 3.0   | 7437 | 1.8310          |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.17.0
- Tokenizers 0.10.3
