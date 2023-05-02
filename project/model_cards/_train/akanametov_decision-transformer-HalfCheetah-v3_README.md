---
library_name: transformers
tags:
- HalfCheetah-v3
- deep-reinforcement-learning
- reinforcement-learning
- decision-transformer
model-index:
- name: decision-transformer-HalfCheetah-v3
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: decision_transformer_gym_replay
      type: decision_transformer_gym_replay
    metrics:
    - type: mean_reward
      value: 0.0 +/- 0.0
      name: mean_reward
      verified: false
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# decision-transformer-HalfCheetah-v3

This model is a fine-tuned version of [](https://huggingface.co/) on the decision_transformer_gym_replay dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 64
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 120

### Training results



### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
