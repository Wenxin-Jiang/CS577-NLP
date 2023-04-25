---
tags:
- CartPole-v1
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
      name: CartPole-v1
      type: CartPole-v1
    metrics:
    - type: mean_reward
      value: 301.00 +/- 52.06
      name: mean_reward
      verified: false
---

# (CleanRL) **DQN** Agent Playing **CartPole-v1**

This is a trained model of a DQN agent playing CartPole-v1.
The model was trained by using [CleanRL](https://github.com/vwxyzjn/cleanrl) and the most up-to-date training code can be
found [here](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/dqn.py).

## Command to reproduce the training

```bash
curl -OL https://huggingface.co/cleanrl/CartPole-v1-dqn-seed2/raw/main/dqn.py
curl -OL https://huggingface.co/cleanrl/CartPole-v1-dqn-seed2/raw/main/pyproject.toml
curl -OL https://huggingface.co/cleanrl/CartPole-v1-dqn-seed2/raw/main/poetry.lock
poetry install --all-extras
python dqn.py --save-model --upload-model --hf-entity cleanrl --cuda False --total-timesteps 100000 --seed 2
```

# Hyperparameters
```python
{'batch_size': 128,
 'buffer_size': 10000,
 'capture_video': False,
 'cuda': False,
 'end_e': 0.05,
 'env_id': 'CartPole-v1',
 'exp_name': 'dqn',
 'exploration_fraction': 0.5,
 'gamma': 0.99,
 'hf_entity': 'cleanrl',
 'learning_rate': 0.00025,
 'learning_starts': 10000,
 'save_model': True,
 'seed': 2,
 'start_e': 1,
 'target_network_frequency': 500,
 'torch_deterministic': True,
 'total_timesteps': 100000,
 'track': False,
 'train_frequency': 10,
 'upload_model': True,
 'wandb_entity': None,
 'wandb_project_name': 'cleanRL'}
```
    