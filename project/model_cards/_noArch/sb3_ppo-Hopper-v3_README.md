---
library_name: stable-baselines3
tags:
- Hopper-v3
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: PPO
  results:
  - metrics:
    - type: mean_reward
      value: 2410.11 +/- 9.86
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: Hopper-v3
      type: Hopper-v3
---

# **PPO** Agent playing **Hopper-v3**
This is a trained model of a **PPO** agent playing **Hopper-v3**
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
python -m rl_zoo3.load_from_hub --algo ppo --env Hopper-v3 -orga sb3 -f logs/
python enjoy.py --algo ppo --env Hopper-v3  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo ppo --env Hopper-v3 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo ppo --env Hopper-v3 -f logs/ -orga sb3
```

## Hyperparameters
```python
OrderedDict([('batch_size', 32),
             ('clip_range', 0.2),
             ('ent_coef', 0.00229519),
             ('gae_lambda', 0.99),
             ('gamma', 0.999),
             ('learning_rate', 9.80828e-05),
             ('max_grad_norm', 0.7),
             ('n_envs', 1),
             ('n_epochs', 5),
             ('n_steps', 512),
             ('n_timesteps', 1000000.0),
             ('normalize', True),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs',
              'dict( log_std_init=-2, ortho_init=False, activation_fn=nn.ReLU, '
              'net_arch=[dict(pi=[256, 256], vf=[256, 256])] )'),
             ('vf_coef', 0.835671),
             ('normalize_kwargs', {'norm_obs': True, 'norm_reward': False})])
```
