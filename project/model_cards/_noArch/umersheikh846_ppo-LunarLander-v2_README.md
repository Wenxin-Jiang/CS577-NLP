---
library_name: stable-baselines3
tags:
- LunarLander-v2
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
      name: LunarLander-v2
      type: LunarLander-v2
    metrics:
    - type: mean_reward
      value: 243.69 +/- 18.42
      name: mean_reward
      verified: false
---

# **PPO** Agent playing **LunarLander-v2**
This is a trained model of a **PPO** agent playing **LunarLander-v2**
using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3).

## Usage (with Stable-baselines3)

```python
from huggingface_sb3 import load_from_hub
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy

# Download checkpoint
model_file = load_from_hub("umersheikh846/ppo-LunarLander-v2", "ppo-LunarLander-v2.zip")
# Load the model
model = PPO.load(model_file)

env = make_vec_env("LunarLander-v2", n_envs=1) # for training, 16 n_envs have been used, while 1 enough

# Evaluate the trained model with evaluate policy from SB3
print("Evaluating model")
mean_reward, std_reward = evaluate_policy(model,env, n_eval_episodes=10, deterministic=True)
print(f"Mean reward = {mean_reward:.2f} +/- {std_reward:.2f}")

# Start a new episode
obs = env.reset()

while True:
      action, _states = model.predict(obs, deterministic=True)
      obs, rewards, dones, info = env.step(action)
      env.render()


...
```
