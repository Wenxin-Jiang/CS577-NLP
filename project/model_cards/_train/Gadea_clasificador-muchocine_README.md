---
tags:
- classification
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: clasificador-muchocine
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clasificador-muchocine

This model is a fine-tuned version of [mrm8488/electricidad-base-discriminator](https://huggingface.co/mrm8488/electricidad-base-discriminator) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3790
- Accuracy: 0.4297

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 388  | 1.3752          | 0.3716   |
| 1.4054        | 2.0   | 776  | 1.2843          | 0.4335   |
| 1.0478        | 3.0   | 1164 | 1.3790          | 0.4297   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
