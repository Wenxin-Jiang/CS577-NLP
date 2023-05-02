---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-32-0
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-32-0

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4849
- Accuracy: 0.7716

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
| 0.7059        | 1.0   | 13   | 0.6840          | 0.5385   |
| 0.6595        | 2.0   | 26   | 0.6214          | 0.6923   |
| 0.4153        | 3.0   | 39   | 0.1981          | 0.9231   |
| 0.0733        | 4.0   | 52   | 0.5068          | 0.9231   |
| 0.2092        | 5.0   | 65   | 1.3114          | 0.6923   |
| 0.003         | 6.0   | 78   | 1.1062          | 0.8462   |
| 0.0012        | 7.0   | 91   | 1.5948          | 0.7692   |
| 0.0008        | 8.0   | 104  | 1.6913          | 0.7692   |
| 0.0006        | 9.0   | 117  | 1.7191          | 0.7692   |
| 0.0005        | 10.0  | 130  | 1.6527          | 0.7692   |
| 0.0003        | 11.0  | 143  | 1.4840          | 0.7692   |
| 0.0002        | 12.0  | 156  | 1.3076          | 0.8462   |
| 0.0002        | 13.0  | 169  | 1.3130          | 0.8462   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
