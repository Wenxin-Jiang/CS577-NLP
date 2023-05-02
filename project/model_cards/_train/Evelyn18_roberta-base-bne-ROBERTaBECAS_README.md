---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- becasv2
model-index:
- name: roberta-base-bne-ROBERTaBECAS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-bne-ROBERTaBECAS

This model is a fine-tuned version of [BSC-TeMU/roberta-base-bne](https://huggingface.co/BSC-TeMU/roberta-base-bne) on the becasv2 dataset.
It achieves the following results on the evaluation set:
- Loss: 2.5760

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
- train_batch_size: 11
- eval_batch_size: 11
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 6    | 4.3366          |
| No log        | 2.0   | 12   | 3.1395          |
| No log        | 3.0   | 18   | 2.6092          |
| No log        | 4.0   | 24   | 2.5084          |
| No log        | 5.0   | 30   | 2.5760          |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.9.0+cu111
- Datasets 2.4.0
- Tokenizers 0.12.1
