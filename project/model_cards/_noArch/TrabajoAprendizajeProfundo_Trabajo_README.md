---
tags:
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
---
# TODO: Fill this model card
This is a pre-trained model of agent playing Asteroids-v0 using the [stable-baselines3](https://github.com/DLR-RM/stable-baselines3) library.

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

# Retrieve the model from the hub
## repo_id =  id of the model repository from the Hugging Face Hub (repo_id = {organization}/{repo_name})
## filename = name of the model zip file from the repository
checkpoint = load_from_hub(repo_id="TrabajoAprendizajeProfundo/Trabajo", filename="Asteroids-v0.zip")
model = PPO.load(checkpoint)

# Evaluate the agent
eval_env = gym.make('Asteroids-v0')
mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=10, deterministic=True)
print(f"mean_reward={mean_reward:.2f} +/- {std_reward}")
 
# Watch the agent play
directory = './video'
env = Recorder(env, directory)

obs = env.reset()
done = False
while not done:
  action, _state = model2.predict(obs)
  obs, reward, done, info = env.step(action)

env.play()
```

### Evaluation Results
mean_reward, std_reward = evaluate_policy(model2, eval_env, n_eval_episodes=10)
print(f"mean_reward={mean_reward:.2f} +/- {std_reward}")