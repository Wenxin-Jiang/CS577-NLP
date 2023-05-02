---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-8-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-8-1

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7020
- Accuracy: 0.5008

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
| 0.6773        | 1.0   | 3    | 0.7822          | 0.25     |
| 0.6587        | 2.0   | 6    | 0.8033          | 0.25     |
| 0.693         | 3.0   | 9    | 0.8101          | 0.25     |
| 0.5979        | 4.0   | 12   | 1.1235          | 0.25     |
| 0.4095        | 5.0   | 15   | 1.3563          | 0.25     |
| 0.2836        | 6.0   | 18   | 1.5325          | 0.5      |
| 0.1627        | 7.0   | 21   | 1.7786          | 0.25     |
| 0.0956        | 8.0   | 24   | 2.0067          | 0.5      |
| 0.0535        | 9.0   | 27   | 2.3351          | 0.5      |
| 0.0315        | 10.0  | 30   | 2.6204          | 0.5      |
| 0.0182        | 11.0  | 33   | 2.8483          | 0.5      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
