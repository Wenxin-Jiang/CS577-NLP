---
license: other
tags:
- generated_from_trainer
model-index:
- name: opt-125m-wikitext2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# opt-125m-wikitext2

This model is a fine-tuned version of [facebook/opt-125m](https://huggingface.co/facebook/opt-125m) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.3409

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
| 3.4123        | 1.0   | 2370 | 3.3621          |
| 3.2096        | 2.0   | 4740 | 3.3452          |
| 3.0822        | 3.0   | 7110 | 3.3409          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
