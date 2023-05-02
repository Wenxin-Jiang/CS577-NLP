---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: indobert-hoax-classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# indobert-hoax-classification

This model is a fine-tuned version of [indobenchmark/indobert-base-p1](https://huggingface.co/indobenchmark/indobert-base-p1) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6230
- Accuracy: 0.8059

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4.2173070213315e-05
- train_batch_size: 32
- eval_batch_size: 16
- seed: 30
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 85   | 0.5540          | 0.7029   |
| No log        | 2.0   | 170  | 0.5432          | 0.7029   |
| No log        | 3.0   | 255  | 0.4963          | 0.7441   |
| No log        | 4.0   | 340  | 0.5791          | 0.7971   |
| No log        | 5.0   | 425  | 0.6230          | 0.8059   |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
