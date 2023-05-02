---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- swag
metrics:
- accuracy
model-index:
- name: bert-base-uncased-finetuned-swag-e1-b16-l5e5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-swag-e1-b16-l5e5

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the swag dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5202
- Accuracy: 0.7997

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.701         | 1.0   | 4597 | 0.5202          | 0.7997   |


### Framework versions

- Transformers 4.12.2
- Pytorch 1.9.1
- Datasets 1.12.1
- Tokenizers 0.10.3
