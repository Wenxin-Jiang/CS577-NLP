---
tags:
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
---
# ThomasSimonini/ppo-SpaceInvadersNoFrameskip-v4

This is a pre-trained model of a PPO agent playing SpaceInvadersNoFrameskip using the [stable-baselines3](https://github.com/DLR-RM/stable-baselines3) library. It is taken from [RL-trained-agents](https://github.com/DLR-RM/rl-trained-agents)


### Usage (with Stable-baselines3)
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
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.vec_env import VecFrameStack

# Retrieve the model from the hub
## repo_id =  id of the model repository from the Hugging Face Hub (repo_id = {organization}/{repo_name})
## filename = name of the model zip file from the repository
checkpoint = load_from_hub(repo_id="ThomasSimonini/ppo-SpaceInvadersNoFrameskip-v4", filename="ppo-SpaceInvadersNoFrameskip-v4.zip")
model = PPO.load(checkpoint)
```

### Evaluation Results
Mean_reward: 627.160 (162 eval episodes)

