---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: bert-base-uncased-issues-128
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-issues-128

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2520

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 16

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.0949        | 1.0   | 291  | 1.7072          |
| 1.649         | 2.0   | 582  | 1.4409          |
| 1.4835        | 3.0   | 873  | 1.4099          |
| 1.3938        | 4.0   | 1164 | 1.3858          |
| 1.3326        | 5.0   | 1455 | 1.2004          |
| 1.2949        | 6.0   | 1746 | 1.2955          |
| 1.2451        | 7.0   | 2037 | 1.2682          |
| 1.1992        | 8.0   | 2328 | 1.1938          |
| 1.1784        | 9.0   | 2619 | 1.1686          |
| 1.1397        | 10.0  | 2910 | 1.2050          |
| 1.1293        | 11.0  | 3201 | 1.2058          |
| 1.1006        | 12.0  | 3492 | 1.1680          |
| 1.0835        | 13.0  | 3783 | 1.2414          |
| 1.0757        | 14.0  | 4074 | 1.1522          |
| 1.062         | 15.0  | 4365 | 1.1176          |
| 1.0535        | 16.0  | 4656 | 1.2520          |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.2+cu102
- Datasets 2.1.0
- Tokenizers 0.12.1
