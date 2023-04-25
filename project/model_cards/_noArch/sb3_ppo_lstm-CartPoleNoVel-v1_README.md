---
library_name: stable-baselines3
tags:
- CartPoleNoVel-v1
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: RecurrentPPO
  results:
  - metrics:
    - type: mean_reward
      value: 500.00 +/- 0.00
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: CartPoleNoVel-v1
      type: CartPoleNoVel-v1
---

# **RecurrentPPO** Agent playing **CartPoleNoVel-v1**
This is a trained model of a **RecurrentPPO** agent playing **CartPoleNoVel-v1**
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
python -m rl_zoo3.load_from_hub --algo ppo_lstm --env CartPoleNoVel-v1 -orga sb3 -f logs/
python enjoy.py --algo ppo_lstm --env CartPoleNoVel-v1  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo ppo_lstm --env CartPoleNoVel-v1 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo ppo_lstm --env CartPoleNoVel-v1 -f logs/ -orga sb3
```

## Hyperparameters
```python
OrderedDict([('batch_size', 256),
             ('clip_range', 'lin_0.2'),
             ('ent_coef', 0.0),
             ('gae_lambda', 0.8),
             ('gamma', 0.98),
             ('learning_rate', 'lin_0.001'),
             ('n_envs', 8),
             ('n_epochs', 20),
             ('n_steps', 32),
             ('n_timesteps', 100000.0),
             ('normalize', True),
             ('policy', 'MlpLstmPolicy'),
             ('policy_kwargs',
              'dict( ortho_init=False, activation_fn=nn.ReLU, '
              'lstm_hidden_size=64, enable_critic_lstm=True, '
              'net_arch=[dict(pi=[64], vf=[64])] )'),
             ('normalize_kwargs', {'norm_obs': True, 'norm_reward': False})])
```
