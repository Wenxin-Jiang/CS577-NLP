---
license: mit
tags:
- generated_from_trainer
model-index:
- name: Bundestag-gpt2-large
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Bundestag-gpt2-large

This model is a fine-tuned version of [benjamin/gerpt2-large](https://huggingface.co/benjamin/gerpt2-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.8236

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step   | Validation Loss |
|:-------------:|:-----:|:------:|:---------------:|
| 2.7899        | 1.0   | 32852  | 2.6879          |
| 2.4421        | 2.0   | 65704  | 2.6749          |
| 2.206         | 3.0   | 98556  | 2.7354          |
| 1.9544        | 4.0   | 131408 | 2.8236          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
