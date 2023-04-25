---
license: apache-2.0
tags:
- deep-reinforcement-learning
- reinforcement-learning
---
model-index:
- name: stable-baselines3-ppo-LunarLander-v2
---
# ARCHIVED MODEL, DO NOT USE IT
# stable-baselines3-ppo-LunarLander-v2 🚀👩‍🚀
This is a saved model of a PPO agent playing [LunarLander-v2](https://gym.openai.com/envs/LunarLander-v2/). The model is taken from [rl-baselines3-zoo](https://github.com/DLR-RM/rl-trained-agents)

The goal is to correctly land the lander by controlling firing engines (fire left orientation engine, fire main engine and fire right orientation engine).

<iframe width="560" height="315" src="https://www.youtube.com/embed/kE-Fvht81I0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

👉 You can watch the agent playing by using this [notebook](https://colab.research.google.com/drive/19OonMRkMyCH6Dg0ECFQi7evxMRqkW3U0?usp=sharing)

## Use the Model
### Install the dependencies
You need to use the [Stable Baselines 3 Hugging Face version](https://github.com/simoninithomas/stable-baselines3) of the library (this version contains the function to load saved models directly from the Hugging Face Hub):

```
pip install git+https://github.com/simoninithomas/stable-baselines3.git
```
### Evaluate the agent
⚠️You need to have Linux or MacOS to be able to use this environment. If it's not the case you can use the [colab notebook](https://colab.research.google.com/drive/19OonMRkMyCH6Dg0ECFQi7evxMRqkW3U0#scrollTo=Qbzj9quh0FsP)


```
# Import the libraries
import gym
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

# Load the environment
env = gym.make('LunarLander-v2')

model = PPO.load_from_huggingface(hf_model_id="ThomasSimonini/stable-baselines3-ppo-LunarLander-v2",hf_model_filename="LunarLander-v2")
 
# Evaluate the agent
eval_env = gym.make('LunarLander-v2')
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
```
## Results
Mean Reward (10 evaluation episodes): 245.63 +/- 10.02