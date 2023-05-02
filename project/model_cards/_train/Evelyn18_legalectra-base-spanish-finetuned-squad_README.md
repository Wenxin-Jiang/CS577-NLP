---
tags:
- generated_from_trainer
datasets:
- squad_es
model-index:
- name: legalectra-base-spanish-finetuned-squad
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# legalectra-base-spanish-finetuned-squad

This model is a fine-tuned version of [mrm8488/legalectra-base-spanish](https://huggingface.co/mrm8488/legalectra-base-spanish) on the squad_es dataset.
It achieves the following results on the evaluation set:
- Loss: 5.9506

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 3    | 5.9506          |
| No log        | 2.0   | 6    | 5.9506          |
| No log        | 3.0   | 9    | 5.9506          |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
