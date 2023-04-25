---
library_name: stable-baselines3
tags:
- MountainCarContinuous-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: TQC
  results:
  - metrics:
    - type: mean_reward
      value: 76.40 +/- 38.49
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: MountainCarContinuous-v0
      type: MountainCarContinuous-v0
---

# **TQC** Agent playing **MountainCarContinuous-v0**
This is a trained model of a **TQC** agent playing **MountainCarContinuous-v0**
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
python -m rl_zoo3.load_from_hub --algo tqc --env MountainCarContinuous-v0 -orga sb3 -f logs/
python enjoy.py --algo tqc --env MountainCarContinuous-v0  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo tqc --env MountainCarContinuous-v0 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo tqc --env MountainCarContinuous-v0 -f logs/ -orga sb3
```

## Hyperparameters
```python
OrderedDict([('batch_size', 512),
             ('buffer_size', 50000),
             ('ent_coef', 0.1),
             ('gamma', 0.9999),
             ('gradient_steps', 32),
             ('learning_rate', 0.0003),
             ('learning_starts', 0),
             ('n_timesteps', 50000.0),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs', 'dict(log_std_init=-3.67, net_arch=[64, 64])'),
             ('tau', 0.01),
             ('train_freq', 32),
             ('use_sde', True),
             ('normalize', False)])
```
