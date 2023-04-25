---
license: mit
tags:
- generated_from_trainer
model-index:
- name: xlnet-base-cased-IUChatbot-ontologyDts
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlnet-base-cased-IUChatbot-ontologyDts

This model is a fine-tuned version of [xlnet-base-cased](https://huggingface.co/xlnet-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4965

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 318  | 0.5005          |
| 0.8222        | 2.0   | 636  | 0.4488          |
| 0.8222        | 3.0   | 954  | 0.4965          |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.17.0
- Tokenizers 0.10.3
