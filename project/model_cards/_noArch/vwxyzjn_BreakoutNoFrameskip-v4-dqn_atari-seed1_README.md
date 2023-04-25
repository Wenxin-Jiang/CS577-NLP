---
tags:
- BreakoutNoFrameskip-v4
- deep-reinforcement-learning
- reinforcement-learning
- custom-implementation
model-index:
- name: DQN
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: BreakoutNoFrameskip-v4
      type: BreakoutNoFrameskip-v4
    metrics:
    - type: mean_reward
      value: 2.70 +/- 4.12
      name: mean_reward
      verified: false
---

# (CleanRL) **DQN** Agent Playing **BreakoutNoFrameskip-v4**

This is a trained model of a DQN agent playing BreakoutNoFrameskip-v4.
The model was trained by using [CleanRL](https://github.com/vwxyzjn/cleanrl) and the training code can be
found [here](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/dqn_atari.py).


# Hyperparameters
```python
{'batch_size': 32,
 'buffer_size': 1000000,
 'capture_video': False,
 'cuda': True,
 'end_e': 0.01,
 'env_id': 'BreakoutNoFrameskip-v4',
 'exp_name': 'dqn_atari',
 'exploration_fraction': 0.1,
 'gamma': 0.99,
 'hf_entity': '',
 'learning_rate': 0.0001,
 'learning_starts': 80000,
 'save_model': True,
 'seed': 1,
 'start_e': 1,
 'target_network_frequency': 1000,
 'torch_deterministic': True,
 'total_timesteps': 10000,
 'track': False,
 'train_frequency': 4,
 'upload_model': True,
 'wandb_entity': None,
 'wandb_project_name': 'cleanRL'}
```
    