---
library_name: stable-baselines3
tags:
- Walker2DBulletEnv-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: PPO
  results:
  - metrics:
    - type: mean_reward
      value: 2120.20 +/- 6.34
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: Walker2DBulletEnv-v0
      type: Walker2DBulletEnv-v0
---

# **PPO** Agent playing **Walker2DBulletEnv-v0**
This is a trained model of a **PPO** agent playing **Walker2DBulletEnv-v0**
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
python -m rl_zoo3.load_from_hub --algo ppo --env Walker2DBulletEnv-v0 -orga sb3 -f logs/
python enjoy.py --algo ppo --env Walker2DBulletEnv-v0  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo ppo --env Walker2DBulletEnv-v0 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo ppo --env Walker2DBulletEnv-v0 -f logs/ -orga sb3
```

## Hyperparameters
```python
OrderedDict([('batch_size', 128),
             ('clip_range', 'lin_0.4'),
             ('ent_coef', 0.0),
             ('env_wrapper', 'sb3_contrib.common.wrappers.TimeFeatureWrapper'),
             ('gae_lambda', 0.92),
             ('gamma', 0.99),
             ('learning_rate', 3e-05),
             ('max_grad_norm', 0.5),
             ('n_envs', 16),
             ('n_epochs', 20),
             ('n_steps', 512),
             ('n_timesteps', 2000000.0),
             ('normalize', True),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs',
              'dict(log_std_init=-2, ortho_init=False, activation_fn=nn.ReLU, '
              'net_arch=[dict(pi=[256, 256], vf=[256, 256])] )'),
             ('sde_sample_freq', 4),
             ('use_sde', True),
             ('vf_coef', 0.5),
             ('normalize_kwargs', {'norm_obs': True, 'norm_reward': False})])
```
