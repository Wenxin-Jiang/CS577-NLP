---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-8-7
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-8-7

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7037
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
| 0.6864        | 1.0   | 3    | 0.7800          | 0.25     |
| 0.6483        | 2.0   | 6    | 0.8067          | 0.25     |
| 0.6028        | 3.0   | 9    | 0.8500          | 0.25     |
| 0.4086        | 4.0   | 12   | 1.0661          | 0.25     |
| 0.2923        | 5.0   | 15   | 1.2302          | 0.25     |
| 0.2059        | 6.0   | 18   | 1.0312          | 0.5      |
| 0.1238        | 7.0   | 21   | 1.1271          | 0.5      |
| 0.0711        | 8.0   | 24   | 1.3100          | 0.5      |
| 0.0453        | 9.0   | 27   | 1.4208          | 0.5      |
| 0.0198        | 10.0  | 30   | 1.5988          | 0.5      |
| 0.0135        | 11.0  | 33   | 1.9174          | 0.5      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
