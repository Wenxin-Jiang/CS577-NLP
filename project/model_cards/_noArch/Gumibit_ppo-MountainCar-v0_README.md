---
library_name: stable-baselines3
tags:
- MountainCar-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: PPO
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: MountainCar-v0
      type: MountainCar-v0
    metrics:
    - type: mean_reward
      value: -200.00 +/- 0.00
      name: mean_reward
      verified: false
---

# **PPO** Agent playing **MountainCar-v0**
This is a trained model of a **PPO** agent playing **MountainCar-v0**
using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3).

## Usage (with Stable-baselines3)
TODO: Add your code


```python
from stable_baselines3 import ...
from huggingface_sb3 import load_from_hub

...
```