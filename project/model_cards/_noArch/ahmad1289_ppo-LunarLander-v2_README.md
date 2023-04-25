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
      value: 274.81 +/- 20.36
      name: mean_reward
      verified: false
---

# **PPO** Agent playing **LunarLander-v2**
This is a trained model of a **PPO** agent playing **LunarLander-v2**
using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3).

## Usage (with Stable-baselines3)
TODO: Add your code


```python
from huggingface_hub import notebook_login 
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_vec_env

# Create the environment
env = make_vec_env('LunarLander-v2', n_envs=16)

model = PPO(
    policy = 'MlpPolicy', # The policy to be optimized
    env = env,            # The environment in which the agent will act
    n_steps = 2048,       # The number of steps to run for each environment per update
    batch_size = 64,      # Minibatch size
    n_epochs = 10,         # Number of epoch when optimizing the surrogate loss
    gamma = 0.999,        # discount factor used to weigh future rewards in the total reward calculation
    gae_lambda = 0.98,    # parameter used in the Generalized Advantage Estimation (GAE) algorithm
    ent_coef = 0.01,      # Entropy coefficient for the loss calculation
    verbose=0)            # Verbosity level: 0 for no output, 1 for info messages (such as device or wrappers used), 2 for debug messages

# Train it for 1,500,000 timesteps
model.learn(total_timesteps=1500000, progress_bar=True)
# Specify file name for model and save the model to file
model_name = "ppo-LunarLander-v2"
model.save(model_name)

# Create a new environment for evaluation
eval_env = gym.make("LunarLander-v2")

# Evaluate the model with 10 evaluation episodes and deterministic=True
mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=10, deterministic=True)

# Print the results
print(f"mean_reward={mean_reward:.2f} +/- {std_reward}")
```
