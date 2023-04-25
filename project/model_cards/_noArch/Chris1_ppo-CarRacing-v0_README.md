---
library_name: stable-baselines3
tags:
- CarRacing-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: PPO
  results:
  - metrics:
    - type: mean_reward
      value: 205.45 +/- 120.65
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: CarRacing-v0
      type: CarRacing-v0
---

# **PPO** Agent playing **CarRacing-v0**
This is a trained model of a **PPO** agent playing **CarRacing-v0**
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
python -m utils.load_from_hub --algo ppo --env CarRacing-v0 -orga Chris1 -f logs/
python enjoy.py --algo ppo --env CarRacing-v0  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo ppo --env CarRacing-v0 -f logs/
# Upload the model and generate video (when possible)
python -m utils.push_to_hub --algo ppo --env CarRacing-v0 -f logs/ -orga Chris1
```

## Hyperparameters
```python
OrderedDict([('batch_size', 128),
             ('clip_range', 0.2),
             ('ent_coef', 0.0),
             ('env_wrapper',
              [{'utils.wrappers.FrameSkip': {'skip': 2}},
               {'gym.wrappers.resize_observation.ResizeObservation': {'shape': 64}},
               {'gym.wrappers.gray_scale_observation.GrayScaleObservation': {'keep_dim': True}}]),
             ('frame_stack', 2),
             ('gae_lambda', 0.95),
             ('gamma', 0.99),
             ('learning_rate', 'lin_1e-4'),
             ('max_grad_norm', 0.5),
             ('n_envs', 8),
             ('n_epochs', 10),
             ('n_steps', 512),
             ('n_timesteps', 4000000.0),
             ('normalize', "{'norm_obs': False, 'norm_reward': True}"),
             ('policy', 'CnnPolicy'),
             ('policy_kwargs',
              'dict(log_std_init=-2, ortho_init=False, activation_fn=nn.GELU, '
              'net_arch=[dict(pi=[256], vf=[256])], )'),
             ('sde_sample_freq', 4),
             ('use_sde', True),
             ('vf_coef', 0.5),
             ('normalize_kwargs', {'norm_obs': False, 'norm_reward': False})])
```
