---
library_name: stable-baselines3
tags:
- SpaceInvadersNoFrameskip-v4
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: PPO
  results:
  - metrics:
    - type: mean_reward
      value: 273.00 +/- 82.29
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: SpaceInvadersNoFrameskip-v4
      type: SpaceInvadersNoFrameskip-v4
---

# **PPO** Agent playing **SpaceInvadersNoFrameskip-v4**
This is a trained model of a **PPO** agent playing **SpaceInvadersNoFrameskip-v4**
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
python -m utils.load_from_hub --algo ppo --env SpaceInvadersNoFrameskip-v4 -orga Ambiwlans -f logs/
python enjoy.py --algo ppo --env SpaceInvadersNoFrameskip-v4  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo ppo --env SpaceInvadersNoFrameskip-v4 -f logs/
# Upload the model and generate video (when possible)
python -m utils.push_to_hub --algo ppo --env SpaceInvadersNoFrameskip-v4 -f logs/ -orga Ambiwlans
```

## Hyperparameters
```python
OrderedDict([('batch_size', 256),
             ('clip_range', 'lin_0.1'),
             ('ent_coef', 0.01),
             ('env_wrapper',
              ['stable_baselines3.common.atari_wrappers.AtariWrapper']),
             ('frame_stack', 4),
             ('learning_rate', 'lin_2.5e-4'),
             ('n_envs', 8),
             ('n_epochs', 4),
             ('n_steps', 128),
             ('n_timesteps', 1000000.0),
             ('policy', 'CnnPolicy'),
             ('vf_coef', 0.5),
             ('normalize', False)])
```
