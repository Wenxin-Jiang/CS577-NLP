---
library_name: stable-baselines3
tags:
- LunarLander-v2
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: DQN
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: LunarLander-v2
      type: LunarLander-v2
    metrics:
    - type: mean_reward
      value: -95.66 +/- 135.45
      name: mean_reward
      verified: false
---

# **DQN** Agent playing **LunarLander-v2**
This is a trained model of a **DQN** agent playing **LunarLander-v2**
using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3)
and the [RL Zoo](https://github.com/DLR-RM/rl-baselines3-zoo).

The RL Zoo is a training framework for Stable Baselines3
reinforcement learning agents,
with hyperparameter optimization and pre-trained agents included.

## Usage (with SB3 RL Zoo)

RL Zoo: https://github.com/DLR-RM/rl-baselines3-zoo<br/>
SB3: https://github.com/DLR-RM/stable-baselines3<br/>
SB3 Contrib: https://github.com/Stable-Baselines-Team/stable-baselines3-contrib

Install the RL Zoo (with SB3 and SB3-Contrib):
```bash
pip install rl_zoo3
```

```
# Download model and save it into the logs/ folder
python -m rl_zoo3.load_from_hub --algo dqn --env LunarLander-v2 -orga kreepy -f logs/
python -m rl_zoo3.enjoy --algo dqn --env LunarLander-v2  -f logs/
```

If you installed the RL Zoo3 via pip (`pip install rl_zoo3`), from anywhere you can do:
```
python -m rl_zoo3.load_from_hub --algo dqn --env LunarLander-v2 -orga kreepy -f logs/
python -m rl_zoo3.enjoy --algo dqn --env LunarLander-v2  -f logs/
```

## Training (with the RL Zoo)
```
python -m rl_zoo3.train --algo dqn --env LunarLander-v2 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo dqn --env LunarLander-v2 -f logs/ -orga kreepy
```

## Hyperparameters
```python
OrderedDict([('batch_size', 9),
             ('buffer_size', 56569),
             ('exploration_final_eps', 0.1),
             ('exploration_fraction', 0.1164397832458963),
             ('exploration_initial_eps', 0.03696153798457299),
             ('gamma', 0.0006190974200887802),
             ('gradient_steps', 9),
             ('learning_rate', 0.011288061590135373),
             ('learning_starts', 15731),
             ('max_grad_norm', 3.705892661777349),
             ('n_timesteps', 10000000.0),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs', 'dict(net_arch=[256, 256])'),
             ('target_update_interval', 218430),
             ('tau', 0.04363931503941886),
             ('train_freq', (9, 'episode')),
             ('normalize', False)])
```
