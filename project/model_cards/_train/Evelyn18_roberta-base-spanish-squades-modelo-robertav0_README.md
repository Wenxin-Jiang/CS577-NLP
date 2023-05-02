---
tags:
- generated_from_trainer
datasets:
- becasv2
model-index:
- name: roberta-base-spanish-squades-modelo-robertav0
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-spanish-squades-modelo-robertav0

This model is a fine-tuned version of [IIC/roberta-base-spanish-squades](https://huggingface.co/IIC/roberta-base-spanish-squades) on the becasv2 dataset.
It achieves the following results on the evaluation set:
- Loss: 2.7628

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
- train_batch_size: 11
- eval_batch_size: 11
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 6    | 2.1175          |
| No log        | 2.0   | 12   | 1.7427          |
| No log        | 3.0   | 18   | 2.0810          |
| No log        | 4.0   | 24   | 2.3820          |
| No log        | 5.0   | 30   | 2.5007          |
| No log        | 6.0   | 36   | 2.6782          |
| No log        | 7.0   | 42   | 2.7578          |
| No log        | 8.0   | 48   | 2.7703          |
| No log        | 9.0   | 54   | 2.7654          |
| No log        | 10.0  | 60   | 2.7628          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
