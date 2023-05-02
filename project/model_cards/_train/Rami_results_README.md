---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: results
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# results

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3691
- Micro f1: 0.3798
- Macro f1: 0.0172

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 512
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Micro f1 | Macro f1 |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| No log        | 1.0   | 4    | 0.6471          | 0.0960   | 0.0322   |
| No log        | 2.0   | 8    | 0.5902          | 0.2933   | 0.0364   |
| No log        | 3.0   | 12   | 0.5430          | 0.3700   | 0.0345   |
| No log        | 4.0   | 16   | 0.5061          | 0.3709   | 0.0307   |
| No log        | 5.0   | 20   | 0.4765          | 0.3756   | 0.0216   |
| No log        | 6.0   | 24   | 0.4524          | 0.3748   | 0.0179   |
| No log        | 7.0   | 28   | 0.4326          | 0.3788   | 0.0173   |
| No log        | 8.0   | 32   | 0.4160          | 0.3803   | 0.0173   |
| No log        | 9.0   | 36   | 0.4027          | 0.3798   | 0.0172   |
| No log        | 10.0  | 40   | 0.3920          | 0.3798   | 0.0172   |
| No log        | 11.0  | 44   | 0.3836          | 0.3798   | 0.0172   |
| No log        | 12.0  | 48   | 0.3773          | 0.3798   | 0.0172   |
| No log        | 13.0  | 52   | 0.3728          | 0.3798   | 0.0172   |
| No log        | 14.0  | 56   | 0.3701          | 0.3798   | 0.0172   |
| No log        | 15.0  | 60   | 0.3691          | 0.3798   | 0.0172   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
