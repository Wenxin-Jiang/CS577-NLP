---
library_name: stable-baselines3
tags:
- BipedalWalker-v3
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: RecurrentPPO
  results:
  - metrics:
    - type: mean_reward
      value: 240.11 +/- 82.53
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: BipedalWalker-v3
      type: BipedalWalker-v3
---

# **RecurrentPPO** Agent playing **BipedalWalker-v3**
This is a trained model of a **RecurrentPPO** agent playing **BipedalWalker-v3**
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
python -m utils.load_from_hub --algo ppo_lstm --env BipedalWalker-v3 -orga Chris1 -f logs/
python enjoy.py --algo ppo_lstm --env BipedalWalker-v3  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo ppo_lstm --env BipedalWalker-v3 -f logs/
# Upload the model and generate video (when possible)
python -m utils.push_to_hub --algo ppo_lstm --env BipedalWalker-v3 -f logs/ -orga Chris1
```

## Hyperparameters
```python
OrderedDict([('batch_size', 256),
             ('clip_range', 0.18),
             ('ent_coef', 0.0),
             ('gae_lambda', 0.95),
             ('gamma', 0.999),
             ('learning_rate', 0.0003),
             ('n_envs', 32),
             ('n_epochs', 10),
             ('n_steps', 256),
             ('n_timesteps', 5000000.0),
             ('normalize', True),
             ('policy', 'MlpLstmPolicy'),
             ('policy_kwargs',
              'dict( ortho_init=False, activation_fn=nn.ReLU, '
              'lstm_hidden_size=64, enable_critic_lstm=True, '
              'net_arch=[dict(pi=[64], vf=[64])] )'),
             ('normalize_kwargs', {'norm_obs': True, 'norm_reward': False})])
```
