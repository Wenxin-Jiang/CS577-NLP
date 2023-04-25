---
library_name: stable-baselines3
tags:
- seals/CartPole-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: PPO
  results:
  - metrics:
    - type: mean_reward
      value: 500.00 +/- 0.00
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: seals/CartPole-v0
      type: seals/CartPole-v0
---

# **PPO** Agent playing **seals/CartPole-v0**
This is a trained model of a **PPO** agent playing **seals/CartPole-v0**
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
python -m rl_zoo3.load_from_hub --algo ppo --env seals/CartPole-v0 -orga ernestumorga -f logs/
python enjoy.py --algo ppo --env seals/CartPole-v0  -f logs/
```

If you installed the RL Zoo3 via pip (`pip install rl_zoo3`), from anywhere you can do:
```
python -m rl_zoo3.load_from_hub --algo ppo --env seals/CartPole-v0 -orga ernestumorga -f logs/
rl_zoo3 enjoy --algo ppo --env seals/CartPole-v0  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo ppo --env seals/CartPole-v0 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo ppo --env seals/CartPole-v0 -f logs/ -orga ernestumorga
```

## Hyperparameters
```python
OrderedDict([('batch_size', 256),
             ('clip_range', 0.4),
             ('ent_coef', 0.008508727919228772),
             ('gae_lambda', 0.9),
             ('gamma', 0.9999),
             ('learning_rate', 0.0012403278189645594),
             ('max_grad_norm', 0.8),
             ('n_envs', 8),
             ('n_epochs', 10),
             ('n_steps', 512),
             ('n_timesteps', 100000.0),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs',
              {'activation_fn': <class 'torch.nn.modules.activation.ReLU'>,
               'net_arch': [{'pi': [64, 64], 'vf': [64, 64]}]}),
             ('vf_coef', 0.489343896591493),
             ('normalize', False)])
```
