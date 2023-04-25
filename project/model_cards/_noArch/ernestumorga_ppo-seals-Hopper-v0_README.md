---
library_name: stable-baselines3
tags:
- seals/Hopper-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: PPO
  results:
  - metrics:
    - type: mean_reward
      value: 2228.87 +/- 43.40
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: seals/Hopper-v0
      type: seals/Hopper-v0
---

# **PPO** Agent playing **seals/Hopper-v0**
This is a trained model of a **PPO** agent playing **seals/Hopper-v0**
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
python -m utils.load_from_hub --algo ppo --env seals/Hopper-v0 -orga ernestumorga -f logs/
python enjoy.py --algo ppo --env seals/Hopper-v0  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo ppo --env seals/Hopper-v0 -f logs/
# Upload the model and generate video (when possible)
python -m utils.push_to_hub --algo ppo --env seals/Hopper-v0 -f logs/ -orga ernestumorga
```

## Hyperparameters
```python
OrderedDict([('batch_size', 512),
             ('clip_range', 0.1),
             ('ent_coef', 0.0010159833764878474),
             ('gae_lambda', 0.98),
             ('gamma', 0.995),
             ('learning_rate', 0.0003904770450788824),
             ('max_grad_norm', 0.9),
             ('n_envs', 1),
             ('n_epochs', 20),
             ('n_steps', 2048),
             ('n_timesteps', 1000000.0),
             ('normalize', True),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs',
              'dict(activation_fn=nn.ReLU, net_arch=[dict(pi=[64, 64], vf=[64, '
              '64])])'),
             ('vf_coef', 0.20315938606555833),
             ('normalize_kwargs', {'norm_obs': True, 'norm_reward': False})])
```
