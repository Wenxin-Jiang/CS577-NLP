---
library_name: stable-baselines3
tags:
- seals/Hopper-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: SAC
  results:
  - metrics:
    - type: mean_reward
      value: 1350.71 +/- 25.77
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: seals/Hopper-v0
      type: seals/Hopper-v0
---

# **SAC** Agent playing **seals/Hopper-v0**
This is a trained model of a **SAC** agent playing **seals/Hopper-v0**
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
python -m rl_zoo3.load_from_hub --algo sac --env seals/Hopper-v0 -orga HumanCompatibleAI -f logs/
python enjoy.py --algo sac --env seals/Hopper-v0  -f logs/
```

If you installed the RL Zoo3 via pip (`pip install rl_zoo3`), from anywhere you can do:
```
python -m rl_zoo3.load_from_hub --algo sac --env seals/Hopper-v0 -orga HumanCompatibleAI -f logs/
rl_zoo3 enjoy --algo sac --env seals/Hopper-v0  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo sac --env seals/Hopper-v0 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo sac --env seals/Hopper-v0 -f logs/ -orga HumanCompatibleAI
```

## Hyperparameters
```python
OrderedDict([('batch_size', 128),
             ('buffer_size', 100000),
             ('gamma', 0.98),
             ('learning_rate', 0.001709807687567946),
             ('learning_starts', 1000),
             ('n_timesteps', 1000000.0),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs',
              {'log_std_init': -1.6829391077276037,
               'net_arch': [256, 256],
               'use_sde': False}),
             ('tau', 0.08),
             ('train_freq', 32),
             ('normalize', False)])
```
