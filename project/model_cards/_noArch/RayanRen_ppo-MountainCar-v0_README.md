---
library_name: stable-baselines3
tags:
- MountainCar-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: PPO
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: MountainCar-v0
      type: MountainCar-v0
    metrics:
    - type: mean_reward
      value: -109.40 +/- 8.96
      name: mean_reward
      verified: false
---

# **PPO** Agent playing **MountainCar-v0**
This is a trained model of a **PPO** agent playing **MountainCar-v0**
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
python -m rl_zoo3.load_from_hub --algo ppo --env MountainCar-v0 -orga RayanRen -f logs/
python enjoy.py --algo ppo --env MountainCar-v0  -f logs/
```

If you installed the RL Zoo3 via pip (`pip install rl_zoo3`), from anywhere you can do:
```
python -m rl_zoo3.load_from_hub --algo ppo --env MountainCar-v0 -orga RayanRen -f logs/
rl_zoo3 enjoy --algo ppo --env MountainCar-v0  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo ppo --env MountainCar-v0 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo ppo --env MountainCar-v0 -f logs/ -orga RayanRen
```

## Hyperparameters
```python
OrderedDict([('ent_coef', 0.0),
             ('gae_lambda', 0.98),
             ('gamma', 0.99),
             ('n_envs', 16),
             ('n_epochs', 4),
             ('n_steps', 16),
             ('n_timesteps', 1000000.0),
             ('normalize', True),
             ('policy', 'MlpPolicy'),
             ('normalize_kwargs', {'norm_obs': True, 'norm_reward': False})])
```
