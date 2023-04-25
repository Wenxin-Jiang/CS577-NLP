---
library_name: stable-baselines3
tags:
- LunarLanderContinuous-v2
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: TRPO
  results:
  - metrics:
    - type: mean_reward
      value: 273.95 +/- 23.86
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: LunarLanderContinuous-v2
      type: LunarLanderContinuous-v2
---

# **TRPO** Agent playing **LunarLanderContinuous-v2**
This is a trained model of a **TRPO** agent playing **LunarLanderContinuous-v2**
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
python -m rl_zoo3.load_from_hub --algo trpo --env LunarLanderContinuous-v2 -orga sb3 -f logs/
python enjoy.py --algo trpo --env LunarLanderContinuous-v2  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo trpo --env LunarLanderContinuous-v2 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo trpo --env LunarLanderContinuous-v2 -f logs/ -orga sb3
```

## Hyperparameters
```python
OrderedDict([('n_critic_updates', 20),
             ('n_envs', 2),
             ('n_steps', 1024),
             ('n_timesteps', 200000.0),
             ('normalize', True),
             ('policy', 'MlpPolicy'),
             ('normalize_kwargs', {'norm_obs': True, 'norm_reward': False})])
```