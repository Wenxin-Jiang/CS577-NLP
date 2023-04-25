---
library_name: stable-baselines3
tags:
- PendulumNoVel-v1
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: RecurrentPPO
  results:
  - metrics:
    - type: mean_reward
      value: -266.92 +/- 180.41
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: PendulumNoVel-v1
      type: PendulumNoVel-v1
---

# **RecurrentPPO** Agent playing **PendulumNoVel-v1**
This is a trained model of a **RecurrentPPO** agent playing **PendulumNoVel-v1**
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
python -m rl_zoo3.load_from_hub --algo ppo_lstm --env PendulumNoVel-v1 -orga sb3 -f logs/
python enjoy.py --algo ppo_lstm --env PendulumNoVel-v1  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo ppo_lstm --env PendulumNoVel-v1 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo ppo_lstm --env PendulumNoVel-v1 -f logs/ -orga sb3
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
             ('normalize', True),
             ('policy', 'MlpLstmPolicy'),
             ('policy_kwargs',
              'dict( ortho_init=False, activation_fn=nn.ReLU, '
              'lstm_hidden_size=64, enable_critic_lstm=True, '
              'net_arch=[dict(pi=[64], vf=[64])] )'),
             ('sde_sample_freq', 4),
             ('use_sde', True),
             ('normalize_kwargs', {'norm_obs': True, 'norm_reward': False})])
```
