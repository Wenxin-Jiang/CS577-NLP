---
license: cc-by-4.0
tags:
- generated_from_trainer
datasets:
- squad_v2
model-index:
- name: roberta-base-squad2-finetuned-squad2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-squad2-finetuned-squad2

This model is a fine-tuned version of [deepset/roberta-base-squad2](https://huggingface.co/deepset/roberta-base-squad2) on the squad_v2 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8815

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.6979        | 1.0   | 16478 | 0.8815          |


### Framework versions

- Transformers 4.19.4
- Pytorch 1.8.1+cu111
- Datasets 2.2.2
- Tokenizers 0.12.1
