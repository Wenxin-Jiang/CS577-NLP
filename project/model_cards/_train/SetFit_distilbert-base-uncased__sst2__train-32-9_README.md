---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-32-9
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-32-9

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5625
- Accuracy: 0.7353

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
| 0.7057        | 1.0   | 13   | 0.6805          | 0.5385   |
| 0.6642        | 2.0   | 26   | 0.6526          | 0.7692   |
| 0.5869        | 3.0   | 39   | 0.5773          | 0.8462   |
| 0.4085        | 4.0   | 52   | 0.4959          | 0.8462   |
| 0.2181        | 5.0   | 65   | 0.4902          | 0.6923   |
| 0.069         | 6.0   | 78   | 0.5065          | 0.8462   |
| 0.0522        | 7.0   | 91   | 0.6082          | 0.7692   |
| 0.0135        | 8.0   | 104  | 0.6924          | 0.7692   |
| 0.0084        | 9.0   | 117  | 0.5921          | 0.7692   |
| 0.0061        | 10.0  | 130  | 0.6477          | 0.7692   |
| 0.0047        | 11.0  | 143  | 0.6648          | 0.7692   |
| 0.0035        | 12.0  | 156  | 0.6640          | 0.7692   |
| 0.0031        | 13.0  | 169  | 0.6615          | 0.7692   |
| 0.0029        | 14.0  | 182  | 0.6605          | 0.7692   |
| 0.0026        | 15.0  | 195  | 0.6538          | 0.8462   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
