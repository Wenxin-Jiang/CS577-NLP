---
library_name: stable-baselines3
tags:
- seals/Swimmer-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: SAC
  results:
  - metrics:
    - type: mean_reward
      value: 27.34 +/- 1.27
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: seals/Swimmer-v0
      type: seals/Swimmer-v0
---

# **SAC** Agent playing **seals/Swimmer-v0**
This is a trained model of a **SAC** agent playing **seals/Swimmer-v0**
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
python -m utils.load_from_hub --algo sac --env seals/Swimmer-v0 -orga ernestumorga -f logs/
python enjoy.py --algo sac --env seals/Swimmer-v0  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo sac --env seals/Swimmer-v0 -f logs/
# Upload the model and generate video (when possible)
python -m utils.push_to_hub --algo sac --env seals/Swimmer-v0 -f logs/ -orga ernestumorga
```

## Hyperparameters
```python
OrderedDict([('batch_size', 128),
             ('buffer_size', 100000),
             ('gamma', 0.995),
             ('learning_rate', 0.00039981805535514633),
             ('learning_starts', 1000),
             ('n_timesteps', 1000000.0),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs',
              'dict(net_arch=[400, 300], log_std_init=-2.689958330139309)'),
             ('tau', 0.01),
             ('train_freq', 256),
             ('normalize', False)])
```
