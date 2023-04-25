---
tags:
- PongNoFrameskip-v4
- deep-reinforcement-learning
- reinforcement-learning
- custom-implementation
library_name: cleanrl
model-index:
- name: DQN
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: PongNoFrameskip-v4
      type: PongNoFrameskip-v4
    metrics:
    - type: mean_reward
      value: 19.70 +/- 1.35
      name: mean_reward
      verified: false
---

# (CleanRL) **DQN** Agent Playing **PongNoFrameskip-v4**

This is a trained model of a DQN agent playing PongNoFrameskip-v4.
The model was trained by using [CleanRL](https://github.com/vwxyzjn/cleanrl) and the most up-to-date training code can be
found [here](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/dqn_atari_jax.py).

## Command to reproduce the training

```bash
curl -OL https://huggingface.co/cleanrl/PongNoFrameskip-v4-dqn_atari_jax-seed1/raw/main/dqn.py
curl -OL https://huggingface.co/cleanrl/PongNoFrameskip-v4-dqn_atari_jax-seed1/raw/main/pyproject.toml
curl -OL https://huggingface.co/cleanrl/PongNoFrameskip-v4-dqn_atari_jax-seed1/raw/main/poetry.lock
poetry install --all-extras
python dqn_atari_jax.py --track --capture-video --save-model --upload-model --hf-entity cleanrl --env-id PongNoFrameskip-v4 --seed 1
```

# Hyperparameters
```python
{'batch_size': 32,
 'buffer_size': 1000000,
 'capture_video': True,
 'end_e': 0.01,
 'env_id': 'PongNoFrameskip-v4',
 'exp_name': 'dqn_atari_jax',
 'exploration_fraction': 0.1,
 'gamma': 0.99,
 'hf_entity': 'cleanrl',
 'learning_rate': 0.0001,
 'learning_starts': 80000,
 'save_model': True,
 'seed': 1,
 'start_e': 1,
 'target_network_frequency': 1000,
 'total_timesteps': 10000000,
 'track': True,
 'train_frequency': 4,
 'upload_model': True,
 'wandb_entity': None,
 'wandb_project_name': 'cleanRL'}
```
    