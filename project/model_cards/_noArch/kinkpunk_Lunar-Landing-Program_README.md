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
      value: 285.36 +/- 14.99
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
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_vec_env

repo_id = "kinkpunk/Lunar-Landing-Program" 
filename = "LunarProgram-PPO.zip" 

custom_objects = {
            "learning_rate": 0.0,
            "lr_schedule": lambda _: 0.0,
            "clip_range": lambda _: 0.0,
}

checkpoint = load_from_hub(repo_id, filename)
model = PPO.load(checkpoint,
                 custom_objects=custom_objects,
                 print_system_info=True)

env = make_vec_env('LunarLander-v2', n_envs=1)

# Evaluate the model
mean_reward, std_reward = evaluate_policy(model, env,
                                          n_eval_episodes=10,
                                          deterministic=True)
# Print the results
print('mean_reward={:.2f} +/- {:.2f}'.format(mean_reward, std_reward))
```

## Training (with Stable-baselines3)
```python
from huggingface_sb3 import load_from_hub

from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_vec_env

# Create the evaluation envs
env = make_vec_env('LunarLander-v2', n_envs=16)
env = gym.make('LunarLander-v2')

# Instantiate the agent
model = PPO(
    policy = 'MlpPolicy',
    env = env,
    n_steps = 1024,
    batch_size = 32,
    n_epochs = 8,
    gamma = 0.99,
    gae_lambda = 0.95,
    ent_coef = 0.01,
    verbose=1,
    seed=2022)

# Train
model.learn(total_timesteps=1500000)
# Save model
model_name = "Any-Name"
model.save(model_name)
```
