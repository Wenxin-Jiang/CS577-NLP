---
library_name: stable-baselines3
tags:
- LunarLander-v2
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: A2C
  results:
  - metrics:
    - type: mean_reward
      value: 181.08 +/- 95.35
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: LunarLander-v2
      type: LunarLander-v2
---

# **A2C** Agent playing **LunarLander-v2**
This is a trained model of a **A2C** agent playing **LunarLander-v2**
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
python -m rl_zoo3.load_from_hub --algo a2c --env LunarLander-v2 -orga sb3 -f logs/
python enjoy.py --algo a2c --env LunarLander-v2  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo a2c --env LunarLander-v2 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo a2c --env LunarLander-v2 -f logs/ -orga sb3
```

## Hyperparameters
```python
OrderedDict([('ent_coef', 1e-05),
             ('gamma', 0.995),
             ('learning_rate', 'lin_0.00083'),
             ('n_envs', 8),
             ('n_steps', 5),
             ('n_timesteps', 200000.0),
             ('policy', 'MlpPolicy'),
             ('normalize', False)])
```
