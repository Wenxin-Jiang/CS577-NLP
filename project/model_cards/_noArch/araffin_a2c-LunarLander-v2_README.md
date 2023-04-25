---
library_name: stable-baselines3
tags:
- LunarLander-v2
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: A2C
  results:
  - metrics:
    - type: mean_reward
      value: 111.57 +/- 98.19
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: LunarLander-v2
      type: LunarLander-v2
---

  # **A2C** Agent playing **LunarLander-v2**
  This is a trained model of a **A2C** agent playing **LunarLander-v2** using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3).
  
## Usage (with Stable-Baselines3)

```python
from huggingface_sb3 import load_from_hub
from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy

# Download checkpoint
checkpoint = load_from_hub("araffin/a2c-LunarLander-v2", "a2c-LunarLander-v2.zip")
# Load the model
model = A2C.load(checkpoint)

env = make_vec_env("LunarLander-v2", n_envs=1)

# Evaluate
print("Evaluating model")
mean_reward, std_reward = evaluate_policy(
    model,
    env,
    n_eval_episodes=20,
    deterministic=True,
)
print(f"Mean reward = {mean_reward:.2f} +/- {std_reward:.2f}")

# Start a new episode
obs = env.reset()

try:
    while True:
        action, _states = model.predict(obs, deterministic=True)
        obs, rewards, dones, info = env.step(action)
        env.render()
except KeyboardInterrupt:
    pass

```
  
  ## Training code (with Stable-baselines3)
```python
from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.callbacks import EvalCallback

# Create the environment
env_id = "LunarLander-v2"
n_envs = 8
env = make_vec_env(env_id, n_envs=n_envs)

# Create the evaluation envs
eval_envs = make_vec_env(env_id, n_envs=5)

# Adjust evaluation interval depending on the number of envs
eval_freq = int(1e5)
eval_freq = max(eval_freq // n_envs, 1)

# Create evaluation callback to save best model
# and monitor agent performance
eval_callback = EvalCallback(
    eval_envs,
    best_model_save_path="./logs/",
    eval_freq=eval_freq,
    n_eval_episodes=10,
)


# Instantiate the agent
# Hyperparameters from https://github.com/DLR-RM/rl-baselines3-zoo
linear_schedule = lambda progress_remaining: progress_remaining * 0.00083
model = A2C(
    "MlpPolicy",
    env,
    n_steps=5,
    gamma=0.995,
    learning_rate=linear_schedule,
    ent_coef=0.00001,
    verbose=1,
)

# Train the agent (you can kill it before using ctrl+c)
try:
    model.learn(total_timesteps=int(5e5), callback=eval_callback)
except KeyboardInterrupt:
    pass

# Load best model
model = A2C.load("logs/best_model.zip")
```
  