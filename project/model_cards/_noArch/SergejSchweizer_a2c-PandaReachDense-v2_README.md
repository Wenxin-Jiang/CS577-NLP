---
library_name: stable-baselines3
tags:
- PandaReachDense-v2
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: A2C
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: PandaReachDense-v2
      type: PandaReachDense-v2
    metrics:
    - type: mean_reward
      value: -2.78 +/- 0.58
      name: mean_reward
      verified: false
---

# **A2C** Agent playing **PandaReachDense-v2**
This is a trained model of a **A2C** agent playing **PandaReachDense-v2**
using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3).

## Usage (with Stable-baselines3)
TODO: Add your code


```python
from stable_baselines3 import ...
from huggingface_sb3 import load_from_hub

...
```
