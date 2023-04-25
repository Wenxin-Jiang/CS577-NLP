---
library_name: stable-baselines3
tags:
- MountainCarContinuous-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: PPO
  results:
  - metrics:
    - type: mean_reward
      value: -0.00 +/- 0.00
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: MountainCarContinuous-v0
      type: MountainCarContinuous-v0
---

# **PPO** Agent playing **MountainCarContinuous-v0**
This is a trained model of a **PPO** agent playing **MountainCarContinuous-v0**
using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3).

## Usage (with Stable-baselines3)

```python
from stable_baselines3 import PPO
from huggingface_sb3 import load_from_hub

# load and create the model
model_path = load_from_hub("danieladejumo/ppo-mountan_car_continuous", 
                           "ppo-mountan_car_continuous.zip")
model = PPO.load(model_path)

# create Mountain Car Continuous environment and evaluate the trained agent
env = gym.make("MountainCarContinuous-v0")
mean_return, std_return = evaluate_policy(model, env, n_eval_episodes=50, deterministic=True)
```
