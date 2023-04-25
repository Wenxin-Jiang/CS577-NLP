---
library_name: stable-baselines3
tags:
- seals/MountainCar-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: PPO
  results:
  - metrics:
    - type: mean_reward
      value: -100.60 +/- 5.75
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: seals/MountainCar-v0
      type: seals/MountainCar-v0
---

# **PPO** Agent playing **seals/MountainCar-v0**
This is a trained model of a **PPO** agent playing **seals/MountainCar-v0**
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
python -m rl_zoo3.load_from_hub --algo ppo --env seals/MountainCar-v0 -orga ernestumorga -f logs/
python enjoy.py --algo ppo --env seals/MountainCar-v0  -f logs/
```

If you installed the RL Zoo3 via pip (`pip install rl_zoo3`), from anywhere you can do:
```
python -m rl_zoo3.load_from_hub --algo ppo --env seals/MountainCar-v0 -orga ernestumorga -f logs/
rl_zoo3 enjoy --algo ppo --env seals/MountainCar-v0  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo ppo --env seals/MountainCar-v0 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo ppo --env seals/MountainCar-v0 -f logs/ -orga ernestumorga
```

## Hyperparameters
```python
OrderedDict([('batch_size', 512),
             ('clip_range', 0.2),
             ('ent_coef', 6.4940755116195606e-06),
             ('gae_lambda', 0.98),
             ('gamma', 0.99),
             ('learning_rate', 0.0004476103728105138),
             ('max_grad_norm', 1),
             ('n_envs', 16),
             ('n_epochs', 20),
             ('n_steps', 256),
             ('n_timesteps', 1000000.0),
             ('normalize', 'dict(norm_obs=False, norm_reward=True)'),
             ('policy',
              'imitation.policies.base.MlpPolicyWithNormalizeFeaturesExtractor'),
             ('policy_kwargs',
              'dict(activation_fn=nn.Tanh, net_arch=[dict(pi=[64, 64], vf=[64, '
              '64])])'),
             ('vf_coef', 0.25988158989488963),
             ('normalize_kwargs', {'norm_obs': False, 'norm_reward': False})])
```
