---
library_name: stable-baselines3
tags:
- CartPole-v1
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: QRDQN
  results:
  - metrics:
    - type: mean_reward
      value: 500.00 +/- 0.00
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: CartPole-v1
      type: CartPole-v1
---

# **QRDQN** Agent playing **CartPole-v1**
This is a trained model of a **QRDQN** agent playing **CartPole-v1**
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
python -m rl_zoo3.load_from_hub --algo qrdqn --env CartPole-v1 -orga sb3 -f logs/
python enjoy.py --algo qrdqn --env CartPole-v1  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo qrdqn --env CartPole-v1 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo qrdqn --env CartPole-v1 -f logs/ -orga sb3
```

## Hyperparameters
```python
OrderedDict([('batch_size', 64),
             ('buffer_size', 100000),
             ('exploration_final_eps', 0.04),
             ('exploration_fraction', 0.16),
             ('gamma', 0.99),
             ('gradient_steps', 128),
             ('learning_rate', 0.0023),
             ('learning_starts', 1000),
             ('n_timesteps', 50000.0),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs', 'dict(net_arch=[256, 256], n_quantiles=10)'),
             ('target_update_interval', 10),
             ('train_freq', 256),
             ('normalize', False)])
```
