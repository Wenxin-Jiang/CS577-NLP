---
library_name: stable-baselines3
tags:
- seals/HalfCheetah-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: SAC
  results:
  - metrics:
    - type: mean_reward
      value: 1474.73 +/- 33.37
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: seals/HalfCheetah-v0
      type: seals/HalfCheetah-v0
---

# **SAC** Agent playing **seals/HalfCheetah-v0**
This is a trained model of a **SAC** agent playing **seals/HalfCheetah-v0**
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
python -m utils.load_from_hub --algo sac --env seals/HalfCheetah-v0 -orga ernestumorga -f logs/
python enjoy.py --algo sac --env seals/HalfCheetah-v0  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo sac --env seals/HalfCheetah-v0 -f logs/
# Upload the model and generate video (when possible)
python -m utils.push_to_hub --algo sac --env seals/HalfCheetah-v0 -f logs/ -orga ernestumorga
```

## Hyperparameters
```python
OrderedDict([('batch_size', 2048),
             ('buffer_size', 100000),
             ('gamma', 0.95),
             ('learning_rate', 0.000884624878315995),
             ('learning_starts', 10000),
             ('n_timesteps', 1000000.0),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs',
              'dict(net_arch=[64, 64], log_std_init=-0.6932709443503001)'),
             ('tau', 0.01),
             ('train_freq', 64),
             ('normalize', False)])
```
