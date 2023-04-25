---
library_name: stable-baselines3
tags:
- Ant-v3
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: TD3
  results:
  - metrics:
    - type: mean_reward
      value: 5822.96 +/- 93.33
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: Ant-v3
      type: Ant-v3
---

# **TD3** Agent playing **Ant-v3**
This is a trained model of a **TD3** agent playing **Ant-v3**
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
python -m rl_zoo3.load_from_hub --algo td3 --env Ant-v3 -orga sb3 -f logs/
python enjoy.py --algo td3 --env Ant-v3  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo td3 --env Ant-v3 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo td3 --env Ant-v3 -f logs/ -orga sb3
```

## Hyperparameters
```python
OrderedDict([('learning_starts', 10000),
             ('n_timesteps', 1000000.0),
             ('policy', 'MlpPolicy'),
             ('normalize', False)])
```
