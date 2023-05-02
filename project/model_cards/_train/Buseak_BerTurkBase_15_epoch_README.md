---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: BerTurkBase_15_epoch
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BerTurkBase_15_epoch

This model is a fine-tuned version of [dbmdz/bert-base-turkish-cased](https://huggingface.co/dbmdz/bert-base-turkish-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0005
- Accuracy: 1.0

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
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 50   | 0.6526          | 0.5972   |
| No log        | 2.0   | 100  | 0.1755          | 0.9653   |
| No log        | 3.0   | 150  | 0.0518          | 0.9861   |
| No log        | 4.0   | 200  | 0.0065          | 1.0      |
| No log        | 5.0   | 250  | 0.0022          | 1.0      |
| No log        | 6.0   | 300  | 0.0016          | 1.0      |
| No log        | 7.0   | 350  | 0.0007          | 1.0      |
| No log        | 8.0   | 400  | 0.0005          | 1.0      |
| No log        | 9.0   | 450  | 0.0005          | 1.0      |
| 0.1362        | 10.0  | 500  | 0.0005          | 1.0      |
| 0.1362        | 11.0  | 550  | 0.0006          | 1.0      |
| 0.1362        | 12.0  | 600  | 0.0005          | 1.0      |
| 0.1362        | 13.0  | 650  | 0.0005          | 1.0      |
| 0.1362        | 14.0  | 700  | 0.0005          | 1.0      |
| 0.1362        | 15.0  | 750  | 0.0005          | 1.0      |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
