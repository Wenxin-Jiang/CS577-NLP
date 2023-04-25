---
tags:
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
---
# ppo-Walker2DBulletEnv-v0

This is a pre-trained model of a PPO agent playing AntBulletEnv-v0 using the [stable-baselines3](https://github.com/DLR-RM/stable-baselines3) library.

### Usage (with Stable-baselines3)
Using this model becomes easy when you have stable-baselines3 and huggingface_sb3 installed:
```
pip install stable-baselines3
pip install huggingface_sb3
```

Then, you can use the model like this:

```python

import gym
import pybullet_envs

from huggingface_sb3 import load_from_hub

from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv, VecNormalize
from stable_baselines3.common.evaluation import evaluate_policy

# Retrieve the model from the hub
## repo_id =  id of the model repository from the Hugging Face Hub (repo_id = {organization}/{repo_name})
## filename = name of the model zip file from the repository
repo_id = "ThomasSimonini/ppo-AntBulletEnv-v0"
checkpoint = load_from_hub(repo_id = repo_id, filename="ppo-AntBulletEnv-v0.zip")
model = PPO.load(checkpoint)

# Load the saved statistics
stats_path = load_from_hub(repo_id = repo_id, filename="vec_normalize.pkl")

eval_env = DummyVecEnv([lambda: gym.make("AntBulletEnv-v0")])
eval_env = VecNormalize.load(stats_path, eval_env)
#  do not update them at test time
eval_env.training = False
# reward normalization is not needed at test time
eval_env.norm_reward = False

from stable_baselines3.common.evaluation import evaluate_policy

mean_reward, std_reward = evaluate_policy(model, eval_env)
print(f"Mean reward = {mean_reward:.2f} +/- {std_reward:.2f}")

```

### Evaluation Results
Mean_reward: 3547.01 +/- 33.32
