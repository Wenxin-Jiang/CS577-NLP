---
library_name: stable-baselines3
tags:
- HopperBulletEnv-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: SAC
  results:
  - metrics:
    - type: mean_reward
      value: 2592.61 +/- 97.32
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: HopperBulletEnv-v0
      type: HopperBulletEnv-v0
---

# **SAC** Agent playing **HopperBulletEnv-v0**
This is a trained model of a **SAC** agent playing **HopperBulletEnv-v0**
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
python -m rl_zoo3.load_from_hub --algo sac --env HopperBulletEnv-v0 -orga sb3 -f logs/
python enjoy.py --algo sac --env HopperBulletEnv-v0  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo sac --env HopperBulletEnv-v0 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo sac --env HopperBulletEnv-v0 -f logs/ -orga sb3
```

## Hyperparameters
```python
OrderedDict([('batch_size', 256),
             ('buffer_size', 300000),
             ('ent_coef', 'auto'),
             ('env_wrapper', 'sb3_contrib.common.wrappers.TimeFeatureWrapper'),
             ('gamma', 0.98),
             ('gradient_steps', 64),
             ('learning_rate', 'lin_7.3e-4'),
             ('learning_starts', 10000),
             ('n_timesteps', 1000000.0),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs', 'dict(log_std_init=-3, net_arch=[400, 300])'),
             ('tau', 0.02),
             ('train_freq', 64),
             ('use_sde', True),
             ('normalize', False)])
```
