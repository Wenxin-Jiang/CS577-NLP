---
library_name: stable-baselines3
tags:
- FingerTurnHardDMC-v0
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
      name: FingerTurnHardDMC-v0
      type: FingerTurnHardDMC-v0
    metrics:
    - type: mean_reward
      value: 277.30 +/- 423.78
      name: mean_reward
      verified: false
---

# **DDPG** Agent playing **FingerTurnHardDMC-v0**
This is a trained model of a **DDPG** agent playing **FingerTurnHardDMC-v0**
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
python -m rl_zoo3.load_from_hub --algo ddpg --env FingerTurnHardDMC-v0 -orga qgallouedec -f logs/
python -m rl_zoo3.enjoy --algo ddpg --env FingerTurnHardDMC-v0  -f logs/
```

If you installed the RL Zoo3 via pip (`pip install rl_zoo3`), from anywhere you can do:
```
python -m rl_zoo3.load_from_hub --algo ddpg --env FingerTurnHardDMC-v0 -orga qgallouedec -f logs/
python -m rl_zoo3.enjoy --algo ddpg --env FingerTurnHardDMC-v0  -f logs/
```

## Training (with the RL Zoo)
```
python -m rl_zoo3.train --algo ddpg --env FingerTurnHardDMC-v0 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo ddpg --env FingerTurnHardDMC-v0 -f logs/ -orga qgallouedec
```

## Hyperparameters
```python
OrderedDict([('batch_size', 64),
             ('gamma', 0.99),
             ('learning_rate', 0.0001),
             ('n_timesteps', 1000000.0),
             ('noise_std', 0.3),
             ('noise_type', 'ornstein-uhlenbeck'),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs',
              'dict(net_arch=dict(pi=[300, 200], qf=[400, 300]))'),
             ('normalize', False)])
```
