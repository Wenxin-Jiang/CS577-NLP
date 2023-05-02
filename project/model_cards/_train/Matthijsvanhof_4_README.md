---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: '4'
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 4

This model is a fine-tuned version of [GroNLP/bert-base-dutch-cased](https://huggingface.co/GroNLP/bert-base-dutch-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1243
- Precision: 0.5220
- Recall: 0.6137
- F1: 0.5641
- Accuracy: 0.9630

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
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 134  | 0.1357          | 0.4549    | 0.5521 | 0.4988 | 0.9574   |
| No log        | 2.0   | 268  | 0.1243          | 0.5220    | 0.6137 | 0.5641 | 0.9630   |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.10.0+cu111
- Tokenizers 0.10.3
