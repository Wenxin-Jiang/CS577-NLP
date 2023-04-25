---
library_name: stable-baselines3
tags:
- SpaceInvadersNoFrameskip-v4
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: A2C
  results:
  - metrics:
    - type: mean_reward
      value: 803.50 +/- 323.72
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: SpaceInvadersNoFrameskip-v4
      type: SpaceInvadersNoFrameskip-v4
---

# **A2C** Agent playing **SpaceInvadersNoFrameskip-v4**
This is a trained model of a **A2C** agent playing **SpaceInvadersNoFrameskip-v4**
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
python -m rl_zoo3.load_from_hub --algo a2c --env SpaceInvadersNoFrameskip-v4 -orga sb3 -f logs/
python enjoy.py --algo a2c --env SpaceInvadersNoFrameskip-v4  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo a2c --env SpaceInvadersNoFrameskip-v4 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo a2c --env SpaceInvadersNoFrameskip-v4 -f logs/ -orga sb3
```

## Hyperparameters
```python
OrderedDict([('ent_coef', 0.01),
             ('env_wrapper',
              ['stable_baselines3.common.atari_wrappers.AtariWrapper']),
             ('frame_stack', 4),
             ('n_envs', 16),
             ('n_timesteps', 10000000.0),
             ('policy', 'CnnPolicy'),
             ('policy_kwargs',
              'dict(optimizer_class=RMSpropTFLike, '
              'optimizer_kwargs=dict(eps=1e-5))'),
             ('vf_coef', 0.25),
             ('normalize', False)])
```
