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
      value: 253.91 +/- 68.63
      name: mean_reward
      verified: false
---

# **PPO** Agent playing **LunarLander-v2**
This is a trained model of a **PPO** agent playing **LunarLander-v2**
using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3).

## Usage (with Stable-baselines3)

```python
import gym

from huggingface_sb3 import load_from_hub, package_to_hub, push_to_hub
from huggingface_hub import notebook_login # To log to our Hugging Face account to be able to upload models to the Hub.

from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_vec_env

# Create the environment
env = make_vec_env('LunarLander-v2', n_envs=16)

model = PPO(
            policy = 'MlpPolicy',
            env = env,
            n_steps = 1024,
            batch_size = 64,
            n_epochs = 8,
            gamma = 0.995,
            gae_lambda = 1,
            ent_coef = 0.001,
            verbose=1
        )

model.learn(total_timesteps=2_000_000, log_interval=25, progress_bar=True)

model_name = "ppo-LunarLander-v2"

# Evaluate the agent
# Create a new environment for evaluation
eval_env = gym.make("LunarLander-v2")

# Evaluate the model with 10 evaluation episodes and deterministic=True
mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=10, deterministic=True)

# Print the results
print(f"mean_reward={mean_reward:.2f} +/- {std_reward}")

# Upload to Hugging Face Hub
...
```
