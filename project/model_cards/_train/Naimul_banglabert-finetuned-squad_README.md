---
tags:
- generated_from_trainer
datasets:
- squad_bn
model-index:
- name: banglabert-finetuned-squad
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# banglabert-finetuned-squad

This model is a fine-tuned version of [csebuetnlp/banglabert](https://huggingface.co/csebuetnlp/banglabert) on the squad_bn dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4421

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
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.3649        | 1.0   | 7397 | 1.4421          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1