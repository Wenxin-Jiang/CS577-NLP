---
library_name: stable-baselines3
tags:
- MountainCarContinuousNoVel-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: RecurrentPPO
  results:
  - metrics:
    - type: mean_reward
      value: 91.22 +/- 1.89
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: MountainCarContinuousNoVel-v0
      type: MountainCarContinuousNoVel-v0
---

# **RecurrentPPO** Agent playing **MountainCarContinuousNoVel-v0**
This is a trained model of a **RecurrentPPO** agent playing **MountainCarContinuousNoVel-v0**
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
python -m rl_zoo3.load_from_hub --algo ppo_lstm --env MountainCarContinuousNoVel-v0 -orga sb3 -f logs/
python enjoy.py --algo ppo_lstm --env MountainCarContinuousNoVel-v0  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo ppo_lstm --env MountainCarContinuousNoVel-v0 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo ppo_lstm --env MountainCarContinuousNoVel-v0 -f logs/ -orga sb3
```

## Hyperparameters
```python
OrderedDict([('batch_size', 256),
             ('clip_range', 0.1),
             ('ent_coef', 0.00429),
             ('gae_lambda', 0.9),
             ('gamma', 0.9999),
             ('learning_rate', 7.77e-05),
             ('max_grad_norm', 5),
             ('n_envs', 8),
             ('n_epochs', 10),
             ('n_steps', 1024),
             ('n_timesteps', 300000.0),
             ('normalize', True),
             ('policy', 'MlpLstmPolicy'),
             ('policy_kwargs',
              'dict(log_std_init=0.0, ortho_init=False, lstm_hidden_size=32, '
              'enable_critic_lstm=True, net_arch=[dict(pi=[64], vf=[64])])'),
             ('sde_sample_freq', 8),
             ('use_sde', True),
             ('vf_coef', 0.19),
             ('normalize_kwargs', {'norm_obs': True, 'norm_reward': False})])
```
