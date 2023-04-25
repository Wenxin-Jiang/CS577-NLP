---
library_name: stable-baselines3
tags:
- Pendulum-v1
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: PPO
  results:
  - metrics:
    - type: mean_reward
      value: -336.89 +/- 406.36
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: Pendulum-v1
      type: Pendulum-v1
---

# **PPO** Agent playing **Pendulum-v1**
This is a trained model of a **PPO** agent playing **Pendulum-v1**
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
python -m utils.load_from_hub --algo ppo --env Pendulum-v1 -orga HumanCompatibleAI -f logs/
python enjoy.py --algo ppo --env Pendulum-v1  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo ppo --env Pendulum-v1 -f logs/
# Upload the model and generate video (when possible)
python -m utils.push_to_hub --algo ppo --env Pendulum-v1 -f logs/ -orga HumanCompatibleAI
```

## Hyperparameters
```python
OrderedDict([('clip_range', 0.2),
             ('ent_coef', 0.0),
             ('gae_lambda', 0.95),
             ('gamma', 0.9),
             ('learning_rate', 0.001),
             ('n_envs', 4),
             ('n_epochs', 10),
             ('n_steps', 1024),
             ('n_timesteps', 100000.0),
             ('policy', 'MlpPolicy'),
             ('sde_sample_freq', 4),
             ('use_sde', True),
             ('normalize', False)])
```
