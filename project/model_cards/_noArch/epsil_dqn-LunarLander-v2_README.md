---
library_name: stable-baselines3
tags:
- LunarLander-v2
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: DQN
  results:
  - metrics:
    - type: mean_reward
      value: -112.74 +/- 52.58
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: LunarLander-v2
      type: LunarLander-v2
---

  # **DQN** Agent playing **LunarLander-v2**
  This is a trained model of a **DQN** agent playing **LunarLander-v2** using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3).
  
  ## Usage (with Stable-baselines3)
```
import gym

from huggingface_sb3 import load_from_hub
from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy

# Retrieve the model from the hub
## repo_id =  id of the model repository from the Hugging Face Hub (repo_id = {organization}/{repo_name})
## filename = name of the model zip file from the repository
checkpoint = load_from_hub(repo_id="epsil/dqn-LunarLander-v2", filename="dqn-LunarLander-v2.zip")

model = DQN.load(checkpoint)

# Evaluate the agent
eval_env = gym.make('LunarLander-v2')
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
  