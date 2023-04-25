---
library_name: stable-baselines3
tags:
- LunarLander-v2
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: QRDQN
  results:
  - metrics:
    - type: mean_reward
      value: 61.43 +/- 184.22
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: LunarLander-v2
      type: LunarLander-v2
---

# **QRDQN** Agent playing **LunarLander-v2**
This is a trained model of a **QRDQN** agent playing **LunarLander-v2**
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
python -m rl_zoo3.load_from_hub --algo qrdqn --env LunarLander-v2 -orga sb3 -f logs/
python enjoy.py --algo qrdqn --env LunarLander-v2  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo qrdqn --env LunarLander-v2 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo qrdqn --env LunarLander-v2 -f logs/ -orga sb3
```

## Hyperparameters
```python
OrderedDict([('batch_size', 128),
             ('buffer_size', 100000),
             ('exploration_final_eps', 0.18),
             ('exploration_fraction', 0.24),
             ('gamma', 0.995),
             ('gradient_steps', -1),
             ('learning_rate', 'lin_1.5e-3'),
             ('learning_starts', 10000),
             ('n_timesteps', 100000.0),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs', 'dict(net_arch=[256, 256], n_quantiles=170)'),
             ('target_update_interval', 1),
             ('train_freq', 256),
             ('normalize', False)])
```
