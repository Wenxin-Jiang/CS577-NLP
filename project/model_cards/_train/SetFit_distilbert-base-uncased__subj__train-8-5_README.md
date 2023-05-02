---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__subj__train-8-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__subj__train-8-5

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6927
- Accuracy: 0.506

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
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.7102        | 1.0   | 3    | 0.6790          | 0.75     |
| 0.6693        | 2.0   | 6    | 0.6831          | 0.75     |
| 0.6438        | 3.0   | 9    | 0.6876          | 0.75     |
| 0.6047        | 4.0   | 12   | 0.6970          | 0.75     |
| 0.547         | 5.0   | 15   | 0.7065          | 0.75     |
| 0.4885        | 6.0   | 18   | 0.7114          | 0.75     |
| 0.4601        | 7.0   | 21   | 0.7147          | 0.5      |
| 0.4017        | 8.0   | 24   | 0.7178          | 0.5      |
| 0.3474        | 9.0   | 27   | 0.7145          | 0.5      |
| 0.2624        | 10.0  | 30   | 0.7153          | 0.5      |
| 0.2175        | 11.0  | 33   | 0.7158          | 0.5      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
