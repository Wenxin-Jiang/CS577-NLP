---
tags:
- generated_from_trainer
model-index:
- name: albert-base-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-base-v2

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0075

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.024         | 1.0   | 4000  | 0.0300          |
| 0.0049        | 2.0   | 8000  | 0.0075          |
| 0.0           | 3.0   | 12000 | 0.0125          |
| 0.0           | 4.0   | 16000 | 0.0101          |
| 0.0056        | 5.0   | 20000 | 0.0104          |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.9.0
- Datasets 2.1.0
- Tokenizers 0.12.1
