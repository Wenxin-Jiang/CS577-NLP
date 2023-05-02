---
language: 
- pt
license: mit
tags:
- generated_from_trainer
model-index:
- name: gpt2-small-portuguese-finetuned-tcu-acordaos
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-small-portuguese-finetuned-tcu-acordaos

This model is a fine-tuned version of [pierreguillou/gpt2-small-portuguese](https://huggingface.co/pierreguillou/gpt2-small-portuguese) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6841

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.3435        | 1.0   | 658  | 1.8346          |
| 1.8668        | 2.0   | 1316 | 1.7141          |
| 1.7573        | 3.0   | 1974 | 1.6841          |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0+cu111
- Datasets 1.13.3
- Tokenizers 0.10.3
