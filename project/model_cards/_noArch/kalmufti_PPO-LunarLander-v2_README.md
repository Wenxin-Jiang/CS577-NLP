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
  - metrics:
    - type: mean_reward
      value: 275.34 +/- 14.56
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: LunarLander-v2
      type: LunarLander-v2
---

  # **PPO** Agent Playing **LunarLander-v2**
  This is a trained model of a **PPO** agent playing **LunarLander-v2** using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3).
  
  ## Usage (with Stable-baselines3, and huggingface_sb3)
  To use this model make sure you are running Python version 3.7.13. You can use [pyenv](https://github.com/pyenv/pyenv) to manage multiple versions of Python on your system.
  
  ### Install required packages:
  ```bash
pip install stable-baselines3
pip install huggingface_sb3
pip install pickle5
pip install Box2D
pip install pyglet
```

You can use this simple script as a base to evaluate and run the model: 
```python
import gym
from stable_baselines3 import PPO
from huggingface_sb3 import load_from_hub
from stable_baselines3.common.evaluation import evaluate_policy

# Download the model from the huggingface hub
checkpoint = load_from_hub(
    repo_id="kalmufti/PPO-LunarLander-v2",
    filename="ppo-LunarLander-v2.zip",
)
# Load the policy
model = PPO.load(checkpoint)
# Create an environment
env = gym.make("LunarLander-v2")
# Optional - evaluate the agent means
mean_reward, std_reward = evaluate_policy(
    model, env, render=False, n_eval_episodes=5, deterministic=True, warn=False
)
print(f"mean_reward={mean_reward:.2f} +/- {std_reward}")

# Watch the agent playing the environment
obs = env.reset()
for i in range(1000):
    action, _state = model.predict(obs)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
        obs = env.reset()
env.close()
```