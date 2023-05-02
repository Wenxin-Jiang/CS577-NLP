---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__subj__all-train
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__subj__all-train

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3193
- Accuracy: 0.9485

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
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.1992        | 1.0   | 500  | 0.1236          | 0.963    |
| 0.084         | 2.0   | 1000 | 0.1428          | 0.963    |
| 0.0333        | 3.0   | 1500 | 0.1906          | 0.965    |
| 0.0159        | 4.0   | 2000 | 0.3193          | 0.9485   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu102
- Datasets 1.17.0
- Tokenizers 0.10.3
