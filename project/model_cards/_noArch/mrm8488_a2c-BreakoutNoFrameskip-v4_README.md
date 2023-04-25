#@title
---
tags:
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
- ATARI
- Breakout
---
# A2C Breakout (No frame skip) v4 🤖🎮

This is a pre-trained model of a A2C agent playing Breakout (NoFrameskip-v4) using the [stable-baselines3](https://github.com/DLR-RM/stable-baselines3) library.

<video loop="" autoplay="" controls="" src="https://huggingface.co/mrm8488/a2c-BreakoutNoFrameskip-v4/resolve/main/output.mp4"></video>

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
from stable_baselines3 import A2C
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.env_util import make_vec_env

# Retrieve the model from the hub
## repo_id =  id of the model repository from the Hugging Face Hub (repo_id = {organization}/{repo_name})
## filename = name of the model zip file from the repository
checkpoint = load_from_hub(repo_id="mrm8488/a2c-BreakoutNoFrameskip-v4", filename="a2c-BreakoutNoFrameskip-v4.zip")
model = PPO.load(checkpoint)

# Evaluate the agent
eval_env = make_atari_env('BreakoutNoFrameskip-v4')
eval_env = VecFrameStack(eval_env, n_stack=4)
mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=10, deterministic=True)
print(f"mean_reward={mean_reward:.2f} +/- {std_reward}")
 
# Watch the agent play
obs = env.reset()
for i in range(1000):
    action, _state = model.predict(obs)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
        obs = env.reset()
env.close()
```

### Evaluation Results
Mean_reward: mean_reward=242.40 +/- 98.97
