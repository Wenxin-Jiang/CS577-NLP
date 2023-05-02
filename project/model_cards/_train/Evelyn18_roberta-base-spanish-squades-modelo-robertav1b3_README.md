---
tags:
- generated_from_trainer
datasets:
- becasv3
model-index:
- name: roberta-base-spanish-squades-modelo-robertav1b3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-spanish-squades-modelo-robertav1b3

This model is a fine-tuned version of [IIC/roberta-base-spanish-squades](https://huggingface.co/IIC/roberta-base-spanish-squades) on the becasv3 dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3537

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
- train_batch_size: 11
- eval_batch_size: 11
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 6    | 2.0804          |
| No log        | 2.0   | 12   | 1.6591          |
| No log        | 3.0   | 18   | 1.9973          |
| No log        | 4.0   | 24   | 2.1109          |
| No log        | 5.0   | 30   | 2.2085          |
| No log        | 6.0   | 36   | 2.3537          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
