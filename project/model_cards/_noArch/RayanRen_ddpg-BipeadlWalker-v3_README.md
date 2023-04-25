---
library_name: stable-baselines3
tags:
- BipedalWalker-v3
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: DDPG
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: BipedalWalker-v3
      type: BipedalWalker-v3
    metrics:
    - type: mean_reward
      value: 223.18 +/- 101.52
      name: mean_reward
      verified: false
---

# **DDPG** Agent playing **BipedalWalker-v3**
This is a trained model of a **DDPG** agent playing **BipedalWalker-v3**
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
python -m rl_zoo3.load_from_hub --algo ddpg --env BipedalWalker-v3 -orga RayanRen -f logs/
python enjoy.py --algo ddpg --env BipedalWalker-v3  -f logs/
```

If you installed the RL Zoo3 via pip (`pip install rl_zoo3`), from anywhere you can do:
```
python -m rl_zoo3.load_from_hub --algo ddpg --env BipedalWalker-v3 -orga RayanRen -f logs/
rl_zoo3 enjoy --algo ddpg --env BipedalWalker-v3  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo ddpg --env BipedalWalker-v3 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo ddpg --env BipedalWalker-v3 -f logs/ -orga RayanRen
```

## Hyperparameters
```python
OrderedDict([('buffer_size', 200000),
             ('gamma', 0.98),
             ('gradient_steps', -1),
             ('learning_rate', 0.001),
             ('learning_starts', 10000),
             ('n_timesteps', 1000000.0),
             ('noise_std', 0.1),
             ('noise_type', 'normal'),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs', 'dict(net_arch=[400, 300])'),
             ('train_freq', [1, 'episode']),
             ('normalize', False)])
```
