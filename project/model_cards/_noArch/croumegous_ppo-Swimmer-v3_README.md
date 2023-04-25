---
library_name: stable-baselines3
tags:
- Swimmer-v3
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
      name: Swimmer-v3
      type: Swimmer-v3
    metrics:
    - type: mean_reward
      value: 366.72 +/- 0.68
      name: mean_reward
      verified: false
---

# **PPO** Agent playing **Swimmer-v3**
This is a trained model of a **PPO** agent playing **Swimmer-v3**
using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3)
and the [RL Zoo](https://github.com/DLR-RM/rl-baselines3-zoo).

The RL Zoo is a training framework for Stable Baselines3
reinforcement learning agents,
with hyperparameter optimization and pre-trained agents included.

## Usage (with SB3 RL Zoo)

RL Zoo: https://github.com/DLR-RM/rl-baselines3-zoo<br/>
SB3: https://github.com/DLR-RM/stable-baselines3<br/>
SB3 Contrib: https://github.com/Stable-Baselines-Team/stable-baselines3-contrib

Install the RL Zoo (with SB3 and SB3-Contrib):
```bash
pip install rl_zoo3
```

```
# Download model and save it into the logs/ folder
python -m rl_zoo3.load_from_hub --algo ppo --env Swimmer-v3 -orga croumegous -f logs/
python -m rl_zoo3.enjoy --algo ppo --env Swimmer-v3  -f logs/
```

If you installed the RL Zoo3 via pip (`pip install rl_zoo3`), from anywhere you can do:
```
python -m rl_zoo3.load_from_hub --algo ppo --env Swimmer-v3 -orga croumegous -f logs/
python -m rl_zoo3.enjoy --algo ppo --env Swimmer-v3  -f logs/
```

## Training (with the RL Zoo)
```
python -m rl_zoo3.train --algo ppo --env Swimmer-v3 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo ppo --env Swimmer-v3 -f logs/ -orga croumegous
```

## Hyperparameters
```python
OrderedDict([('batch_size', 256),
             ('gae_lambda', 0.98),
             ('gamma', 0.9999),
             ('learning_rate', 0.0006),
             ('n_envs', 4),
             ('n_steps', 1024),
             ('n_timesteps', 1000000.0),
             ('normalize', True),
             ('policy', 'MlpPolicy'),
             ('normalize_kwargs', {'norm_obs': True, 'norm_reward': False})])
```
