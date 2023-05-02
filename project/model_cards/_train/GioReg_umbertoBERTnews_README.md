---
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: umbertoBERTnews
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# umbertoBERTnews

This model is a fine-tuned version of [Musixmatch/umberto-commoncrawl-cased-v1](https://huggingface.co/Musixmatch/umberto-commoncrawl-cased-v1) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0847
- Accuracy: 0.9798
- F1: 0.9798

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
- num_epochs: 2

### Training results



### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
