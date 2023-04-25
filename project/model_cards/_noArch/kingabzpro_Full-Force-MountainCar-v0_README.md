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
  - metrics:
    - type: mean_reward
      value: -200.00 +/- 0.00
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: MountainCar-v0
      type: MountainCar-v0
---

  # **PPO** Agent playing **MountainCar-v0**
  This is a trained model of a **PPO** agent playing **MountainCar-v0** using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3).
  
  ## Usage (with Stable-baselines3)
  Using this model becomes easy when you have stable-baselines3 and huggingface_sb3 installed:
```
pip install stable-baselines3
pip install huggingface_sb3
```
Then, you can use the model like this:
```python
import gym

from huggingface_sb3 import load_from_hub
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

# Retrieve the model from the hub
## repo_id =  id of the model repository from the Hugging Face Hub (repo_id = {organization}/{repo_name})
## filename = name of the model zip file from the repository
checkpoint = load_from_hub(repo_id="kingabzpro/Full-Force-MountainCar-v0", filename="Full-Force-MountainCar-v0.zip")
model = PPO.load(checkpoint)

# Evaluate the agent
eval_env = gym.make('MountainCar-v0')
mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=10, deterministic=True)
print(f"mean_reward={mean_reward:.2f} +/- {std_reward}")
 
# Watch the agent play
obs = eval_env.reset()
for i in range(1000):
    action, _state = model.predict(obs)
    obs, reward, done, info = eval_env.step(action)
    eval_env.render()
    if done:
        obs = eval_env.reset()
eval_env.close()
```
  
  