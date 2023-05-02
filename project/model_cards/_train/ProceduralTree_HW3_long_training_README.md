---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: HW3_long_training
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# HW3_long_training

This model is a fine-tuned version of [bert-base-chinese](https://huggingface.co/bert-base-chinese) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3863
- Accuracy: 0.3029

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.3178        | 1.0   | 3007 | 1.3052          | 0.3169   |
| 1.3991        | 2.0   | 6014 | 1.3863          | 0.3029   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
