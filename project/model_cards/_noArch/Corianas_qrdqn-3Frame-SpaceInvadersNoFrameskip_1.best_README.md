---
library_name: stable-baselines3
tags:
- SpaceInvadersNoFrameskip-v4
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: QRDQN
  results:
  - metrics:
    - type: mean_reward
      value: 1855.50 +/- 869.41
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: SpaceInvadersNoFrameskip-v4
      type: SpaceInvadersNoFrameskip-v4
---

# **QRDQN** Agent playing **SpaceInvadersNoFrameskip-v4**
This is a trained model of a **QRDQN** agent playing **SpaceInvadersNoFrameskip-v4**
using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3)
and the [RL Zoo](https://github.com/DLR-RM/rl-baselines3-zoo).

The RL Zoo is a training framework for Stable Baselines3
reinforcement learning agents,
with hyperparameter optimization and pre-trained agents included.

[W&B report](https://wandb.ai/corianas/sb3/reports/QRDQN-Agent-playing-SpaceInvadersNoFrameskip-v4--VmlldzoyMjA4NDk4)

There is a longer video of this agent playing at [Youtube](https://youtu.be/OmxWdSx0ouY)

## Usage (with SB3 RL Zoo)

RL Zoo: https://github.com/DLR-RM/rl-baselines3-zoo<br/>
SB3: https://github.com/DLR-RM/stable-baselines3<br/>
SB3 Contrib: https://github.com/Stable-Baselines-Team/stable-baselines3-contrib

```
# Download model and save it into the logs/ folder
python -m utils.load_from_hub --algo qrdqn --env SpaceInvadersNoFrameskip-v4 -orga Corianas -f logs/
python enjoy.py --algo qrdqn --env SpaceInvadersNoFrameskip-v4  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo qrdqn --env SpaceInvadersNoFrameskip-v4 -f logs/
# Upload the model and generate video (when possible)
python -m utils.push_to_hub --algo qrdqn --env SpaceInvadersNoFrameskip-v4 -f logs/ -orga Corianas
```

## Hyperparameters
```python
OrderedDict([('env_wrapper',
              ['stable_baselines3.common.atari_wrappers.AtariWrapper']),
             ('exploration_fraction', 0.025),
             ('frame_stack', 3),
             ('n_timesteps', 10000000.0),
             ('optimize_memory_usage', True),
             ('policy', 'CnnPolicy'),
             ('normalize', False)])
```
