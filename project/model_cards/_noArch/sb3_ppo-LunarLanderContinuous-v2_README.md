---
library_name: stable-baselines3
tags:
- LunarLanderContinuous-v2
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: PPO
  results:
  - metrics:
    - type: mean_reward
      value: 274.47 +/- 24.37
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: LunarLanderContinuous-v2
      type: LunarLanderContinuous-v2
---

# **PPO** Agent playing **LunarLanderContinuous-v2**
This is a trained model of a **PPO** agent playing **LunarLanderContinuous-v2**
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
python -m rl_zoo3.load_from_hub --algo ppo --env LunarLanderContinuous-v2 -orga sb3 -f logs/
python enjoy.py --algo ppo --env LunarLanderContinuous-v2  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo ppo --env LunarLanderContinuous-v2 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo ppo --env LunarLanderContinuous-v2 -f logs/ -orga sb3
```

## Hyperparameters
```python
OrderedDict([('batch_size', 64),
             ('ent_coef', 0.01),
             ('gae_lambda', 0.98),
             ('gamma', 0.999),
             ('n_envs', 16),
             ('n_epochs', 4),
             ('n_steps', 1024),
             ('n_timesteps', 1000000.0),
             ('policy', 'MlpPolicy'),
             ('normalize', False)])
```
