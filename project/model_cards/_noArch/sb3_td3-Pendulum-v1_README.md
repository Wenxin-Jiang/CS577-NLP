---
library_name: stable-baselines3
tags:
- Pendulum-v1
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: TD3
  results:
  - metrics:
    - type: mean_reward
      value: -195.99 +/- 119.03
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: Pendulum-v1
      type: Pendulum-v1
---

# **TD3** Agent playing **Pendulum-v1**
This is a trained model of a **TD3** agent playing **Pendulum-v1**
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
python -m rl_zoo3.load_from_hub --algo td3 --env Pendulum-v1 -orga sb3 -f logs/
python enjoy.py --algo td3 --env Pendulum-v1  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo td3 --env Pendulum-v1 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo td3 --env Pendulum-v1 -f logs/ -orga sb3
```

## Hyperparameters
```python
OrderedDict([('buffer_size', 200000),
             ('gamma', 0.98),
             ('gradient_steps', -1),
             ('learning_rate', 0.001),
             ('learning_starts', 10000),
             ('n_timesteps', 20000),
             ('noise_std', 0.1),
             ('noise_type', 'normal'),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs', 'dict(net_arch=[400, 300])'),
             ('train_freq', [1, 'episode']),
             ('normalize', False)])
```
