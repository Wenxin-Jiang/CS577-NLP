---
library_name: stable-baselines3
tags:
- seals/Walker2d-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: PPO
  results:
  - metrics:
    - type: mean_reward
      value: 1429.13 +/- 411.75
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: seals/Walker2d-v0
      type: seals/Walker2d-v0
---

# **PPO** Agent playing **seals/Walker2d-v0**
This is a trained model of a **PPO** agent playing **seals/Walker2d-v0**
using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3)
and the [RL Zoo](https://github.com/DLR-RM/rl-baselines3-zoo).

The RL Zoo is a training framework for Stable Baselines3
reinforcement learning agents,
with hyperparameter optimization and pre-trained agents included.

## Usage (with SB3 RL Zoo)

RL Zoo: https://github.com/DLR-RM/rl-baselines3-zoo<br/>
SB3: https://github.com/DLR-RM/stable-baselines3<br/>
SB3 Contrib: https://github.com/Stable-Baselines-Team/stable-baselines3-contrib

```
# Download model and save it into the logs/ folder
python -m utils.load_from_hub --algo ppo --env seals/Walker2d-v0 -orga ernestumorga -f logs/
python enjoy.py --algo ppo --env seals/Walker2d-v0  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo ppo --env seals/Walker2d-v0 -f logs/
# Upload the model and generate video (when possible)
python -m utils.push_to_hub --algo ppo --env seals/Walker2d-v0 -f logs/ -orga ernestumorga
```

## Hyperparameters
```python
OrderedDict([('batch_size', 8),
             ('clip_range', 0.4),
             ('ent_coef', 0.00013057334805552262),
             ('gae_lambda', 0.92),
             ('gamma', 0.98),
             ('learning_rate', 3.791707778339674e-05),
             ('max_grad_norm', 0.6),
             ('n_envs', 1),
             ('n_epochs', 5),
             ('n_steps', 2048),
             ('n_timesteps', 1000000.0),
             ('normalize', True),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs',
              'dict(activation_fn=nn.ReLU, net_arch=[dict(pi=[256, 256], '
              'vf=[256, 256])])'),
             ('vf_coef', 0.6167177795726859),
             ('normalize_kwargs', {'norm_obs': True, 'norm_reward': False})])
```
