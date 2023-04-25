---
library_name: stable-baselines3
tags:
- LunarLanderContinuous-v2
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: ARS
  results:
  - metrics:
    - type: mean_reward
      value: 207.05 +/- 114.40
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: LunarLanderContinuous-v2
      type: LunarLanderContinuous-v2
---

# **ARS** Agent playing **LunarLanderContinuous-v2**
This is a trained model of a **ARS** agent playing **LunarLanderContinuous-v2**
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
python -m rl_zoo3.load_from_hub --algo ars --env LunarLanderContinuous-v2 -orga sb3 -f logs/
python enjoy.py --algo ars --env LunarLanderContinuous-v2  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo ars --env LunarLanderContinuous-v2 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo ars --env LunarLanderContinuous-v2 -f logs/ -orga sb3
```

## Hyperparameters
```python
OrderedDict([('delta_std', 0.1),
             ('learning_rate', 0.018),
             ('n_delta', 4),
             ('n_envs', 8),
             ('n_timesteps', 2000000.0),
             ('n_top', 1),
             ('normalize', 'dict(norm_obs=True, norm_reward=False)'),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs', 'dict(net_arch=[16])'),
             ('zero_policy', False),
             ('normalize_kwargs', {'norm_obs': True, 'norm_reward': False})])
```
