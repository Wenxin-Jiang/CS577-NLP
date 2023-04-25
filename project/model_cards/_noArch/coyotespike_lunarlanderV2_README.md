---
library_name: stable-baselines3
tags:
- BipedalWalker-v3
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
      name: BipedalWalker-v3
      type: BipedalWalker-v3
    metrics:
    - type: mean_reward
      value: -22.95 +/- 48.84
      name: mean_reward
      verified: false
---

# **PPO** Agent playing **BipedalWalker-v3**
This is a trained model of a **PPO** agent playing **BipedalWalker-v3**
using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3).

## Usage (with Stable-baselines3)
TODO: Add your code


```python
from stable_baselines3 import ...
from huggingface_sb3 import load_from_hub

...
```