---
tags:
- generated_from_trainer
- deep-reinforcement-learning
- reinforcement-learning
- decision-transformer
- gym-continous-control

pipeline_tag: reinforcement-learning
datasets:
- decision_transformer_gym_replay
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Decision Transformer model trained on expert trajectories sampled from the Gym Half Cheetah environment
This is a trained [Decision Transformer](https://arxiv.org/abs/2106.01345) model trained from scratch on expert trajectories sampled from the Gym Half Cheetah environment based on the example [training script](https://github.com/huggingface/blog/blob/main/notebooks/101_train-decision-transformers.ipynb) tutorial provided by HuggingFace

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

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1
