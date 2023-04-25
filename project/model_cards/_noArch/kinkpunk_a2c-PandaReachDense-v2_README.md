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
      value: -1.65 +/- 0.14
      name: mean_reward
      verified: false
---

# **A2C** Agent playing **PandaReachDense-v2**
This is a trained model of a **A2C** agent playing **PandaReachDense-v2**
using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3).

## Usage (with Stable-baselines3)

```python
import pybullet_envs
import panda_gym
import gym

import os

from huggingface_sb3 import load_from_hub, package_to_hub

from stable_baselines3 import A2C
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.vec_env import DummyVecEnv, VecNormalize
from stable_baselines3.common.env_util import make_vec_env

from huggingface_hub import notebook_login

load_model = load_from_hub(
	repo_id="kinkpunk/a2c-PandaReachDense-v2",
	filename="a2c-PandaReachDense-v2.zip",
)

model = A2C.load(load_model)

```
