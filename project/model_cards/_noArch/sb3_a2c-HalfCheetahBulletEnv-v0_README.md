---
library_name: stable-baselines3
tags:
- HalfCheetahBulletEnv-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: A2C
  results:
  - metrics:
    - type: mean_reward
      value: 2112.18 +/- 34.59
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: HalfCheetahBulletEnv-v0
      type: HalfCheetahBulletEnv-v0
---

# **A2C** Agent playing **HalfCheetahBulletEnv-v0**
This is a trained model of a **A2C** agent playing **HalfCheetahBulletEnv-v0**
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
python -m rl_zoo3.load_from_hub --algo a2c --env HalfCheetahBulletEnv-v0 -orga sb3 -f logs/
python enjoy.py --algo a2c --env HalfCheetahBulletEnv-v0  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo a2c --env HalfCheetahBulletEnv-v0 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo a2c --env HalfCheetahBulletEnv-v0 -f logs/ -orga sb3
```

## Hyperparameters
```python
OrderedDict([('ent_coef', 0.0),
             ('env_wrapper', 'sb3_contrib.common.wrappers.TimeFeatureWrapper'),
             ('gae_lambda', 0.9),
             ('gamma', 0.99),
             ('learning_rate', 'lin_0.00096'),
             ('max_grad_norm', 0.5),
             ('n_envs', 4),
             ('n_steps', 8),
             ('n_timesteps', 2000000.0),
             ('normalize', True),
             ('normalize_advantage', False),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs',
              'dict(log_std_init=-2, ortho_init=False, full_std=True)'),
             ('use_rms_prop', True),
             ('use_sde', True),
             ('vf_coef', 0.4),
             ('normalize_kwargs', {'norm_obs': True, 'norm_reward': False})])
```