---
tags:
- generated_from_trainer
datasets:
- becasv2
model-index:
- name: roberta-base-spanish-squades-modelo1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-spanish-squades-modelo1

This model is a fine-tuned version of [IIC/roberta-base-spanish-squades](https://huggingface.co/IIC/roberta-base-spanish-squades) on the becasv2 dataset.
It achieves the following results on the evaluation set:
- Loss: 5.7001

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 11
- eval_batch_size: 11
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 6    | 2.7892          |
| No log        | 2.0   | 12   | 3.7037          |
| No log        | 3.0   | 18   | 5.1221          |
| No log        | 4.0   | 24   | 4.5988          |
| No log        | 5.0   | 30   | 5.9202          |
| No log        | 6.0   | 36   | 5.0345          |
| No log        | 7.0   | 42   | 4.4421          |
| No log        | 8.0   | 48   | 4.6969          |
| No log        | 9.0   | 54   | 5.2084          |
| No log        | 10.0  | 60   | 5.7001          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
