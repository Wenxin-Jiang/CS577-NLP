---
tags:
- generated_from_trainer
model-index:
- name: test-erfan
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# test-erfan

This model is a fine-tuned version of [erfan226/persian-t5-paraphraser](https://huggingface.co/erfan226/persian-t5-paraphraser) on the None dataset.

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
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu   | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:------:|:-------:|
| No log        | 1.0   | 63   | nan             | 13.083 | 15.31   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
