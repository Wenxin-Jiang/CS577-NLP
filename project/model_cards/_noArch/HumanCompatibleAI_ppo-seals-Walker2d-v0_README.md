---
library_name: stable-baselines3
tags:
- seals/Walker2d-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: PPO
  results:
  - metrics:
    - type: mean_reward
      value: 2035.70 +/- 609.93
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: seals/Walker2d-v0
      type: seals/Walker2d-v0
---

# **PPO** Agent playing **seals/Walker2d-v0**
This is a trained model of a **PPO** agent playing **seals/Walker2d-v0**
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
python -m rl_zoo3.load_from_hub --algo ppo --env seals/Walker2d-v0 -orga HumanCompatibleAI -f logs/
python enjoy.py --algo ppo --env seals/Walker2d-v0  -f logs/
```

If you installed the RL Zoo3 via pip (`pip install rl_zoo3`), from anywhere you can do:
```
python -m rl_zoo3.load_from_hub --algo ppo --env seals/Walker2d-v0 -orga HumanCompatibleAI -f logs/
rl_zoo3 enjoy --algo ppo --env seals/Walker2d-v0  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo ppo --env seals/Walker2d-v0 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo ppo --env seals/Walker2d-v0 -f logs/ -orga HumanCompatibleAI
```

## Hyperparameters
```python
OrderedDict([('batch_size', 8),
             ('clip_range', 0.4),
             ('ent_coef', 0.00013057334805552262),
             ('gae_lambda', 0.92),
             ('gamma', 0.98),
             ('learning_rate', 3.791707778339674e-05),
             ('max_grad_norm', 0.6),
             ('n_envs', 1),
             ('n_epochs', 5),
             ('n_steps', 2048),
             ('n_timesteps', 1000000.0),
             ('normalize',
              {'gamma': 0.98, 'norm_obs': False, 'norm_reward': True}),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs',
              {'activation_fn': <class 'torch.nn.modules.activation.ReLU'>,
               'features_extractor_class': <class 'imitation.policies.base.NormalizeFeaturesExtractor'>,
               'net_arch': [{'pi': [256, 256], 'vf': [256, 256]}]}),
             ('vf_coef', 0.6167177795726859),
             ('normalize_kwargs',
              {'norm_obs': {'gamma': 0.98,
                            'norm_obs': False,
                            'norm_reward': True},
               'norm_reward': False})])
```
