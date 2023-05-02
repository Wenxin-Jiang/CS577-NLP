---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- null
model-index:
- name: avengers2
  results:
  - task:
      name: Causal Language Modeling
      type: text-generation
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# avengers2

This model is a fine-tuned version of [distilgpt2](https://huggingface.co/distilgpt2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.0131

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
| No log        | 1.0   | 56   | 3.9588          |
| No log        | 2.0   | 112  | 3.9996          |
| No log        | 3.0   | 168  | 4.0131          |


### Framework versions

- Transformers 4.10.0
- Pytorch 1.9.0
- Datasets 1.2.1
- Tokenizers 0.10.1
