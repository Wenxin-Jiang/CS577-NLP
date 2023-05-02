---
license: other
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: dalio-6.7b-test
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dalio-6.7b-test

This model is a fine-tuned version of [facebook/opt-6.7b](https://huggingface.co/facebook/opt-6.7b) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.6641
- Accuracy: 0.0662

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 8
- total_eval_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 2.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.5958        | 0.31  | 16   | 2.5371          | 0.0659   |
| 2.3784        | 0.62  | 32   | 2.5039          | 0.0670   |
| 2.3578        | 0.92  | 48   | 2.6074          | 0.0654   |
| 1.3819        | 1.23  | 64   | 2.6680          | 0.0658   |
| 1.1529        | 1.54  | 80   | 2.6738          | 0.0665   |
| 1.2938        | 1.85  | 96   | 2.6641          | 0.0662   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
